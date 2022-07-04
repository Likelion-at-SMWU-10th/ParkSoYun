from django.urls import path
from . import views

urlpatterns=[
    path('content/<int:des_id>',views.content, name='content'),
    path('edit/',views.edit,name='edit'),
    path('page/',views.page, name='page'),
    path('formcreate/',views.formcreate, name='formcreate'),
]
