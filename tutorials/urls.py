from django.urls import path 
from .views import TutorialsListView, TuteDetailView

urlpatterns = [
    path('', TutorialsListView.as_view(), name='tuteList'),
    path('<int:pk>/', TuteDetailView.as_view(), name='tute'),

]