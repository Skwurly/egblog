from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.
def index(request):
    posts = Post.objects.order_by('id').reverse()
    return render(request, "blog/post_list.html",{'posts':posts})
