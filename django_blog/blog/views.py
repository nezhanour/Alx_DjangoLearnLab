from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .serializers import PostSerializer
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

def base(request):
    return render(request, "base.html")

def posts_list(request):
    posts  = Post.objects.all().order_by('-published_date')
    return render(request, 'blog/posts_list.html', {'posts': posts})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')  # Redirect to the profile page
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'blog/profile.html')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserChangeForm(instance=request.user)
    return render(request, 'blog/edit_profile.html', {'form' : form})

# Use ListView to display a list of all blog posts
class ListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    

# use DetailView To display a single post,
class DetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

# use CreateView to create new post. Allow authenticated users to create new posts
class CreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# UpdateView for Editing Posts and Allow only the author to update their own posts using UserPassesTestMixin
class UpdateView(LoginRequiredMixin,UserPassesTestMixin , UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

# DeleteView for Deleting Posts and use UserPassesTestMixin to ensure only the author can delete their post
class DeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post-list')
    template_name = 'blog/post_confirm_delete.html'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author