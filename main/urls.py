from django.urls import path
from . import views

urlpatterns = [
    path('', views.master),
    path('maps/', views.maps),
    path('co/', views.co),
    path('climat/', views.climat)
]
