from django.shortcuts import render
from .models import Post

def chart(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'index.html' ,context)

def example(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'examp.html', context)

def example1(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts
    } 
    return render(request, 'example.html', context)   
