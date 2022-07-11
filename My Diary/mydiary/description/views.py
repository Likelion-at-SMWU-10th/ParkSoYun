from time import timezone
from django.shortcuts import redirect, render,get_object_or_404
from .models import Description
from .forms import PageForm
from django.utils import timezone
from .forms import PageForm

def page(request):
    descriptions=Description.objects
    return render(request,'description/page.html',{'descriptions':descriptions})

def content(request, des_id):
    description=get_object_or_404(Description,pk=des_id)
    return render(request,'description/content.html', {'description':description})

def edit(request):
    return render(request,'description/edit.html')

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
