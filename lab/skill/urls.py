from django.urls import path
from . import views


skill_router_urlpatterns = [
    path("skill/", views.index, name="index"),
]
