from rest_framework import serializers
from django.contrib.auth.models import User 

from .models import Profile


class UserSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField(read_only=False)
    profile_description = serializers.SerializerMethodField(read_only=False)

    class Meta:
        model = User 
        fields = [
            'id', 
            'username', 
            'email', 
            'first_name', 
            'last_name', 
            'avatar',
            'profile_description',
            ]
        
    def get_avatar(self, obj):
        return obj.profile.avatar.url
    
    def get_profile_description(self, obj):
        return obj.profile.description
        
    
        