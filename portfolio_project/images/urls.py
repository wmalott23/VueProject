from django.urls import path
from . import views

urlpatterns = [
    path('', views.images_list),
    path('<int:pk>/', views.images_detail)
]