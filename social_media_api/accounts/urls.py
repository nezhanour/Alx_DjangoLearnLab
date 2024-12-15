from django.urls import path
from .views import RegisterUserView, loginUserView, UserProfileView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', loginUserView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
]