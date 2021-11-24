from django.shortcuts import render
from blog.models import Post, Comment

# Create your views here.
def blog_home(request):
    context = Post.objects.all().order_by('-created_on')
    return render(request,'blog_home',context)

def blog_post(request):
    context = Post.objects.get(pk=pk)
    return render(request,'blog_post',context)
