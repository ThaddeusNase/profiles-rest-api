from rest_framework import serializers
from profiles_api import models


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing out APIView"""
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta():
        model = models.UserProfile
        fields = ["id", "email", "name", "password"]
        extra_kwargs = {
            "password": {
                    "write_only": True,
                    "style": {"input_type": "password"}
            }
        }

    def create(self, validated_data):
        user = models.UserProfile.objects.create_user(
            email=validated_data["email"],
            name=validated_data["name"],
            password=validated_data["password"]
        )
        return user



# Serializer für ProfileFeedItem
class ProfileFeedItemSerializer(serializers.ModelSerializer):
    class Meta():
        model = models.ProfileFeedItem
        # id, created_on = haben default values = READ ONLY
        # user_profile und status_text = einzigen Felder die veränderbar sind ("writable")!
        # user_profile = NUR AUTHENTICATED USER! -> AUCH = READ ONLY!!!
        fields = ["id", "user_profile" , "status_text", "created_on"]
        extra_kwargs = {
            "user_profile": {
                "read_only": True
            }
        }

        
