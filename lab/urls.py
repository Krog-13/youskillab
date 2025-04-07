from django.urls import path
from . import views
from .health.urls import health_router_urlpatterns
from .skill.urls import skill_router_urlpatterns


urlpatterns = [
    path("", views.index, name="index"),
]

urlpatterns += health_router_urlpatterns + skill_router_urlpatterns
