from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User, Group
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

from rest_framework import permissions, serializers, status, views, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from .forms import NewUserForm
from .serializers import UserSerializer, MyTokenObtainPairSerializer, RegisterUserSerializer


# Create your views here.

#-------------------- START User Authentication --------------------#


class ObtainTokenPairView(TokenObtainPairView):
    permission_classes = [permissions.AllowAny]
    serializer_class = MyTokenObtainPairSerializer


#-------------------- END   User Authentication --------------------#


#-------------------- START API Endpoints --------------------#


class RegisterUserView(APIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = []
    
    def post(self, request, format='json'):
        serializer = RegisterUserSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)

        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class HelloWorldView(APIView):
    def get(self, request):
        return Response(data={"hello":"world"}, status=status.HTTP_200_OK)

#-------------------- END   API Endpoints --------------------#
