from django.urls import path
from .views import RootView, add_collection_view

urlpatterns = [
    path("", RootView.as_view(), name="index"),
    path("add-collection", add_collection_view, name="add-collection"),
]
