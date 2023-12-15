from django.urls import path
from . import views

urlpatterns = [
    path('healthz', views.healthz),
    path('test', views.test)
]