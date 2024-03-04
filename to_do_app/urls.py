from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:id>/", views.homepage, name="homepage"),
    path("display/", views.display, name="display")
]