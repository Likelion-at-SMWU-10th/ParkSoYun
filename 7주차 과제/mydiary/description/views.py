from django.shortcuts import render,get_object_or_404
from .models import Description

def page(request):
    descriptions=Description.objects
    return render(request,'description/page.html',{'descriptions':descriptions})

def content(request, des_id):
    description=get_object_or_404(Description,pk=des_id)
    return render(request,'description/content.html', {'description':description})

def edit(request):
    return render(request,'description/edit.html')
