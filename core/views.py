from django.shortcuts import render
from .models import Post

def chart(request):
    return render(request, 'index.html')

def example(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'examp.html', context)
