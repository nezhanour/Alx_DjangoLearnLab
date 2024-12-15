from django.urls import path
from .views import RegisterUser, loginUser

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', loginUser.as_view(), name='login')
]