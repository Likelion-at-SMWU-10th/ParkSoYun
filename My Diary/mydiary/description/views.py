from time import timezone
from django.shortcuts import redirect, render,get_object_or_404
from .models import Description, Comment
from .forms import CommentForm, PageForm
from django.utils import timezone
from .forms import PageForm

def page(request):
    descriptions=Description.objects.all()
    return render(request,'description/page.html',{'descriptions':descriptions})

def content(request, des_id):
    description=get_object_or_404(Description,pk=des_id)
    form=CommentForm()
    return render(request,'description/content.html', {'description':description,'form':form})

def formcreate(request):
    if request.method=='POST':
        form=PageForm(request.POST)
        if form.is_valid():
            post=Description()
            post.title=form.cleaned_data['title']
            post.body=form.cleaned_data['body']
            post.pub_date=timezone.now()
            post.save()
            return redirect('page')
    else:
        form=PageForm()
        return render(request, 'description/edit.html',{'form':form})

def modelformcreate(request):
    if request.method=='POST':
        form=PageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('page')
    else:
        form=PageForm()
    return render(request,'description/new.html',{'form':form})

def new(request):
    return render(request,'description/new.html')

def edit(request):
    return render(request,'description/edit.html')

def contentupdate(request, des_id):
    post=get_object_or_404(Description,pk=des_id)
    if request.method=='POST':
        form=PageForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('content',des_id=post.pk)
    else:
        form=PageForm(instance=post)
        return render(request, 'description/edit.html',{'form':form})

def contentdelete(request, des_id):
    post=get_object_or_404(Description, pk=des_id)
    post.delete()
    return redirect('page')

def result(request):
    query=request.GET.get('query','')
    if query:
        des_objects=Description.objects.filter(title__contains=query)
        return render(request, 'description/result.html',{'result':des_objects})
    else:
        return render(request, 'description/result.html',{'error':'검색어를 입력하세요'})

def commentcreate(request, des_id):
    des=get_object_or_404(Description,pk=des_id)
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.description=des
            comment.save()
            
    return redirect('content',des_id=des.pk)

def commentupdate(request,com_id):
    comment=get_object_or_404(Comment,pk=com_id)
    if request.method=='POST':
        form=CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('content',des_id=comment.pk)
    else:
        form=CommentForm(instance=comment)
        return render(request,'description/edit.html',{'form':form})

def commentdelete(request,com_id):
    comment=get_object_or_404(Comment,pk=com_id)
    comment.delete()
    return redirect('content')