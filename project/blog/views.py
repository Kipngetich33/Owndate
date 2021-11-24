from django.shortcuts import render
from blog.models import Category, Post, Comment

# Create your views here.
def blog_home(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        'posts':posts
    }
    return render(request,'blog_home.html',context)

def blog_post(request,pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    context ={
        'post':post,
        'comments':comments
    }
    return render(request,'blog_post.html',context)

# Create your views here.
def blog_category(request,category):
    posts = Post.objects.filter(
        categories__name__contains = category
    ).order_by(
        '-created_on'
    )

    context = {
        'category':category,
        'posts':posts
    }

    return render(request,'blog_category.html',context)
