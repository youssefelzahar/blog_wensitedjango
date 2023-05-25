from django.shortcuts import render
from .models import Post;
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin        

# Create your views here.
"""    def Home(request):
        context={
            'posts':Post.objects.all()
        }
        return render (request,'blog/home.html',context)
"""
def about(request):
    return render(request, 'blog/about.html', {'title': "About Page"})

class PostListView(LoginRequiredMixin,ListView):
    model=Post
    template_name='blog/home.html'
    context_object_name="posts"
    ordering=["-date_posted"]

class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post
    template_name='blog/post_detail.html'

class PostCreate(LoginRequiredMixin,CreateView):
    model = Post
    template_name='blog/create.html'
    fields = ['title', 'content']    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class Update(LoginRequiredMixin,UpdateView):
    model=Post
    template_name='blog/create.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False