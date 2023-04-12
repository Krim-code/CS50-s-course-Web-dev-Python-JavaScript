
from django.urls import path

from .views import WomenAPIList

urlpatterns = [
    path('api/v1/womenlist/', WomenAPIList.as_view()),
    path('api/v1/womenlist/<int:pk>/',WomenAPIList.as_view())
]