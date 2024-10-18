from django.urls import path
from home import views

urlpatterns = [
    path('index/', views.index),
    path("update/<id>/", views.update),
    path("delete/<id>/", views.delete, name='delete'),
]