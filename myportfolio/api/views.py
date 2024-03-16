from django.shortcuts import render
from .models import Profile,Image,Project
from rest_framework.permissions import IsAdminUser
from rest_framework import generics
from .serializer import ProfileSerializer,ImageSerializer,ProjectSerializer
from .models import Profile,Image,Project
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status
# from rest_framework.decorators import api_view



#______________________profile view_________________________
class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

#_______________________project handler______________________
class ProjectList(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

#_____________________image handler View____________________
class ImageList(generics.ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer





#______________________profile view_________________________
class AdminProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAdminUser]
#_____________________image handler View____________________
class AdminImageList(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [IsAdminUser]


#_______________________project handler______________________
class AdminProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAdminUser]

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAdminUser]


class ImageDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [IsAdminUser]

class ProjectDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAdminUser]

class UserLoginView(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        if username and password:
            # Authenticate the user using the provided username and password
            user = authenticate(username=username, password=password)

            if user:
                # If the user is authenticated, generate a token
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key, 'user_id': user.id, 'username': user.username})

        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)