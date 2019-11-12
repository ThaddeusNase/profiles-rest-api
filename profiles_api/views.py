from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated


from .serializers import HelloSerializer, ProfileFeedItemSerializer, UserProfileSerializer
from profiles_api import models
from profiles_api import permissions


# Create your views here.


class HelloApiView(APIView):
    # Test API VIEW
    serializer_class = HelloSerializer

    def get(self, request, format=None):
        """ returns a List of APIView features """

        an_apiview = [
            "uses HTTP methods as functions (get, post, patch, put, delete)",
            "is similar to a traditional Django View",
            "Gives u the most control over ur app-logic",
            "is mapped manually to urls"
        ]

        # da jedes APIView function ein Response_Object zurückgeben muss, welches in JSON umwgeandelt wird -> ...
        json_dict = {
            "message": "Hello",         # "message" = key, "hello" = value
            "an_apiview": an_apiview
        }
        return Response(json_dict)


    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
                )

    def put(self, request):
        return Response({"method": "PUT"})

    def patch(self, request):
        return Response({"method": "PATCH"})


    def delete(self, request):
        return Response({"method": "DELETE"})




class HelloViewSet(viewsets.ViewSet):
    serializer_class = HelloSerializer

    def list(self, request):
        a_viewlist = [
            "uses actions -> list, create, retrieve, updatem partial_update",
            "automatically maps to url using Routers",
            "Provides more functionality with less code"
        ]
        return Response({"message": "hello", "a_viewlist": a_viewlist})


    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hello {name}!"
            return Response({"message": message})

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # retrurn bestimmtes/einzelndes Object -> pk nötig
    # maps to HTTP-Get
    def retrieve(self, request, pk=None):
        return Response({"http_method": "GET"})

    # maps to HTTP-Put
    def update(self, request, pk=None):
        return Response({"http_method": "PUT"})

    # handle updating part of an update
    def partial_update(self, request, pk=None):
        return Response({"http_method": "PATCH"})

    # ViewSet function/action mapt zur http-delete-function/request
    def destroy(self, request, pk=None):
        return Response({"http_method": "DELETE"})



class ProfileViewSet(viewsets.ModelViewSet):
    # handle creating/updating profiles
    serializer_class = UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,) # als Tuple!
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("name", "email", )




class UserLoginApiView(ObtainAuthToken):
    # handle creating user authentication tokens for user -> indem man diesen dabei angibt
    # ordnet dann auth token string einem user zu
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES



# handles creating, reading, updating profileFeedItems
class UserProfileFeedViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (
        permissions.UpdateOwnProfile,
        IsAuthenticated,
    )


    # da ProfileFeedView().user_profile = logged in user ->
    def perform_create(self, serializer):
        serializer.save(user_profile=self.request.user)
