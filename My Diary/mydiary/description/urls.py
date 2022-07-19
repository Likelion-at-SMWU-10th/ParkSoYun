from django.urls import path
from . import views

urlpatterns=[
    path('content/<int:des_id>',views.content, name='content'),
    path('edit/',views.edit,name='edit'),
    path('page/',views.page, name='page'),
    #path('formcreate/',views.formcreate, name='formcreate'),
    path('new/',views.new, name='new'),
    path('modelformcreate/',views.modelformcreate,name='modelformcreate'),
    path('edit/',views.edit,name='edit'),
    path('contentupdate/<int:des_id>',views.contentupdate,name='contentupdate'),
    path('contentdelete/<int:des_id>',views.contentdelete,name='contentdelete'),
    path('result',views.result,name='result'),
    path('commentcreate/<int:des_id>',views.commentcreate,name='commentcreate'),
    path('commentupdate/<int:com_id>',views.commentupdate,name='commentupdate'),
    path('commentdelete/<int:com_id>',views.commentdelete,name='commentdelete'),
]
