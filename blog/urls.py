from django.urls import path
from .views import HomePage, BlogDetailView

urlpatterns = [

    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('', HomePage.as_view(), name='home'),
]