# threads/backend/urls.py
from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from .views import ObtainTokenPairView, RegisterUserView, HelloWorldView

urlpatterns = [
    path('user/create/', RegisterUserView.as_view(), name='create_user'),
    path('token/obtain/', ObtainTokenPairView.as_view(), name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('hello/', HelloWorldView.as_view(), name='hello_world'),
]
