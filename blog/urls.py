from django.urls import path
from .views import HomePage, BlogDetailView, CreateBlogView

urlpatterns = [

    path('post/new/', CreateBlogView.as_view(), name='create_post'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('', HomePage.as_view(), name='home'),
]