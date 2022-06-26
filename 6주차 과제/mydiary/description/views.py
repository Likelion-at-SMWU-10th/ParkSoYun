from django.shortcuts import render

def content(request):
    return render(request,'content.html')

def edit(request):
    return render(request,'edit.html')
