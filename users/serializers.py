from rest_framework import serializers
from django.contrib.auth.models import User 
from blog.models import  Post
from .models import Profile


class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ['username', 'email', 'password']

class PostSerializer (serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['author', 'title', 'content', 'date_posted']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'image']
