from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('predict/', views.predict, name='predict'),
    path('predict/', views.predict, name='predict'),
    path('about/', views.about, name='about'),
    path('predict1/', views.predict1, name='predict1'),
    path('data/', views.data, name='data'),
path('viewimage/', views.viewimage, name='viewimage'),
path('viewplot/', views.viewplot, name='viewplot'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)