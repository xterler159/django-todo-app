from django.urls import path
from .views import RootView, process_add_collection

urlpatterns = [
    path("", RootView.as_view(), name="index"),
    path("add-collection", process_add_collection, name="add-collection"),
]
