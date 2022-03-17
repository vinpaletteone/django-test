from pydoc_data.topics import topics
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index),
    path('create/', views.create),
    path('read/<id>', views.read),
    path('delete/', views.delete)
]