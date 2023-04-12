
from django.urls import path

from .views import WomenAPIList, WomenAPIUpdate, WomenAPIDetailView

urlpatterns = [
    path('api/v1/womenlist/', WomenAPIList.as_view()),
    path('api/v1/womenlist/<int:pk>/',WomenAPIUpdate.as_view()),
    path('api/v1/womendetail/<int:pk>/',WomenAPIDetailView.as_view())
]