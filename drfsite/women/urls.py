
from django.urls import path

from .views import WomenAPIView

urlpatterns = [
    path('api/v1/womenlist/', WomenAPIView.as_view()),
    path('api/v1/womenlist/<int:pk>/',WomenAPIView.as_view())
]