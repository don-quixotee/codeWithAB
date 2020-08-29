from django.urls import path 
from .views import blogListView,BlogDetailView

urlpatterns = [
    path('',blogListView.as_view(),name='blogList'),
    path('<int:pk>', BlogDetailView.as_view(), name='blog'),
    ]