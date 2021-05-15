from .serializers import UserSerializer, PostSerializer, ProfileSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User
from blog.models import Post
from .models import Profile

class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewset(viewsets.ModelViewSet):
    queryset= User.objects.all()
    serializer_class = UserSerializer

class ProfileViewset(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer