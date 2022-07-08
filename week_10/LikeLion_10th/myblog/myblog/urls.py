from django.contrib import admin
from django.urls import path, include
from blogapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.home, name='home'),
    path('', views.blog, name='blog'),
    path('detail/<int:blog_id>', views.detail, name='detail'),
    path('community/', views.community, name='community'),
    path('new/',views.new, name='new'),
    path('modelformcreate',views.modelformcreate, name="modelformcreate"),
    path('blogupdate/<int:blog_id>',views.blogupdate, name='blogupdate'),
    path('edit/',views.edit,name='edit'),
    path('blogdelete/<int:blog_id>',views.blogdelete, name='blogdelete'),
]
