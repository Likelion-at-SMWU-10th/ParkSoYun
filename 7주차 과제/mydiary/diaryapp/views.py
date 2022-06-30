from django.shortcuts import render

def home(request):
    return render(request,'diaryapp/home.html')

