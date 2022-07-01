from django.contrib import admin
from django.urls import path, include
from diaryapp import views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('description/',include('description.urls')),
    path('accounts/',include('accounts.urls')),
]
