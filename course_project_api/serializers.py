from rest_framework import serializers

from course_project_api import models


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)


class ProfileSerializer(serializers.ModelSerializer):
    """Serializer for the profile data"""

    class Meta:
        model = models.UserProfile
        fields = ('name', 'email', 'password')
        extra_restriction = {
            'password': {  # when creating a new profile, we can write the password
                'write_only': True,
                'style': {'input_type': 'password'}  # this is only to hide the password when typing it
            }
        }

    def create(self, validated_data):
        """Creat a profile by overriding the default method in the model serializer only to make the password hashed"""
        user = models.UserProfile.objects.create_user(
            name=validated_data['name'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        """we already defined the create_user() method to hash the password"""
        return user


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """for the profile feed items"""

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile':{'read_only':True}}
