from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('content/<int:des_id>',views.content, name='content'),
    path('edit/',views.edit,name='edit'),
    path('page/',views.page, name='page'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings)