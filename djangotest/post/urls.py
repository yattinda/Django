from django.urls import path

from . import views

app_name = 'post'

urlpatterns = [
    path('post_create/', views.post_list, name='post_list'),
    path('', views.post_create, name='post_create'),
]
