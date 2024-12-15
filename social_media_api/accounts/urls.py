from django.urls import path
from .views import RegisterUserView, loginUserView, UserProfileView, FollowUser, UnfollowUser

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', loginUserView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('follow/<int:user_id>/', FollowUser.as_view(), name='follow-user'),
    path('unfollow/<int:user_id>/', UnfollowUser.as_view(), name='unfollow-user'),
]