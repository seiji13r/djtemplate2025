from django.urls import path

from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("base/", TemplateView.as_view(template_name="base.html")),
]