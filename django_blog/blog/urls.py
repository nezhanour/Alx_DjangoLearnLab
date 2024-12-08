from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.base, name='home'),
    path('all_posts/', views.posts_list, name='posts_list'),
    path('posts/', views.ListView.as_view(), name='post-list'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('post/new/', views.CreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', views.DetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', views.UpdateView.as_view(), name='post-edit'),
    path('post/<int:pk>/delete/', views.DeleteView.as_view(), name='post-delete'),
]
