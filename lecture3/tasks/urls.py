from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='tasks_index'),
    path('add', views.add, name='add'),
]