from django.shortcuts import get_object_or_404, render, redirect
from .models import Blog
from django.utils import timezone
from .forms import BlogForm

# Create your views here.
def home(request):
    return render(request, 'blogapp/home.html')

def community(request):
    return render(request, 'blogapp/community.html')

def blog(request):
    blogs = Blog.objects
    return render(request, 'blogapp/home.html', {'blogs': blogs})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'blogapp/detail.html', {'blog': blog_detail})

def new(request):
    return render(request, 'blogapp/new.html')

def create(request):
    if request.method=='POST':
        post=Blog()
        post.title=request.POST['title']
        post.body=request.POST['body']
        post.date=timezone.now()
        post.save()
    return redirect('blog')

def formcreate(request):
    if request.method=='POST':
        form=BlogForm(request.POST)
        if form.is_valid():
            post=Blog()
            post.title=form.cleaned_data['title']
            post.body=form.cleaned_data['body']
            post.date=timezone.now()
            post.save()
            return redirect('blog')
    if request.method=='GET':
        form=BlogForm()
        return render(request, 'blogapp/form_create.html',{'form':form})
