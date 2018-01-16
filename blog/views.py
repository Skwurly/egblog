from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
# Create your views here.
def index(request):
    posts = Post.objects.order_by('id').reverse()
    return render(request, "blog/post_list.html",{'posts':posts})

def post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post.html', {'post':post})
