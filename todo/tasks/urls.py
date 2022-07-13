from django.urls import path
from .views import RootView, process_form

urlpatterns = [
    path("", RootView.as_view(), name="index"),
    path("add-collection", process_form, name="add-collection"),
]
