from django.contrib import admin
from django.urls import include, path
from news import views

urlpatterns = [   
    path('', views.index, name='index'), 
    path('news/', include('news.urls')),
    path('admin/', admin.site.urls),
]
