from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import HelloSerializer

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
