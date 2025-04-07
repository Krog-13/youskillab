from django.urls import path
from . import views

health_router_urlpatterns = [
    path("health/", views.index, name="index"),
]
