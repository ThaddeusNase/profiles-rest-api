from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
    # Test API VIEW
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
