from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone
from .forms import BlogModelForm, CommentForm

# Create your views here.
def home(request):
    return render(request, 'blogapp/home.html')

def blog(request):
    blogs = Blog.objects
    return render(request, 'blogapp/blog.html', {'blogs' : blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    form=CommentForm()
    return render(request, 'blogapp/detail.html', {'blog': blog, 'form':form})

def new(request):
    return render(request, 'blogapp/new.html')

def modelformcreate(request):
    if request.method == 'POST':
        form = BlogModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog')
    else:
        form = BlogModelForm()
    return render(request, 'blogapp/new.html', {'form': form})

def edit(request):
    return render(request, 'blogapp/edit.html')

def blogupdate(request, blog_id):
    post = get_object_or_404(Blog, pk = blog_id)
    if request.method == 'POST':
        form = BlogModelForm(request.POST, instance = post)
        if form.is_valid():
            form.save()
            return redirect('detail', blog_id = post.pk)
    else:
        form = BlogModelForm(instance = post)
        return render(request, 'blogapp/edit.html', {'form': form})

def blogdelete(request, blog_id):
    post = get_object_or_404(Blog, pk = blog_id)
    post.delete()
    return redirect('blog')

def result(request):
    query=request.GET.get('query','')
    if query:
        blog_objects=Blog.objects.filter(title__contains=query)
        return render(request,'blogapp/result.html',{'result':blog_objects})
    else:
        return render(request, 'blogapp/result.html',{'error':'검색어를 입력하세요.'})

def commentcreate(request, blog_id):
    blog=get_object_or_404(Blog,pk=blog_id)
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.blog=blog #comment 모델의 blog(ForeignKey 변수)를 59번째줄 변수 지정한 Blog 객체로 저장
            comment.save()
            return redirect('detail',blog_id=blog.pk)
    return redirect('detail',blog_id=blog.pk)
