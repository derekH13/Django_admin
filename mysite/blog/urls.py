from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.ViewsExercicio.as_view(), name='home'),
    path('posts/', views.PostView.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
]
