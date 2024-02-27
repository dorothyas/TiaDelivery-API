from django.shortcuts import render

from items.models import Items
from .serializers import RegisterSerializer, ProfileSerializer, MyTokenObtainPairSerializer
from items.serializers import ItemsSerializer
from user.models import CustomUser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter

# Create your views here.

#Login User
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

#Register User
class RegisterView(CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

#api/profile  and api/profile/update
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProfile(request):
    user = request.user
    serializer = ProfileSerializer(user, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateProfile(request):
    user = request.user
    serializer = ProfileSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#api/notes
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def getItems(request):
#     # public_items = Items.objects.filter(is_public=True).order_by('-updated')[:10]
#     user_items = request.user.items.all().order_by('-updated')[:10]
#     # notes = public_notes | user_notes
#     items = user_items
#     serializer = ItemsSerializer(items, many=True)
#     return Response(serializer.data)
class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = "http://localhost:8000"
    client_class = OAuth2Client
