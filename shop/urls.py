from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('store/', views.comic_list, name='comic_list'),
    path('store/<slug:category_slug>/', views.comic_list, name='comic_list_by_category'),
    path('comic/<int:id>/<slug:slug>/', views.comic_detail, name='comic_detail'),
]
