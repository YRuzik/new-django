from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('woman/', views.woman, name='woman'),
    path('man/', views.man, name='man'),
    path('children/', views.children , name='children'),
    path('check/', views.product_detail, name='check')
]