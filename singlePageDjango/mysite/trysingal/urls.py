from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('api/<int:page>',views.api, name ="api"),
    path('scroll/<int:page>', views.scroll_gen, name ="scroll_gen"),
    path('scroll', views.scroll, name ="scroll")
]