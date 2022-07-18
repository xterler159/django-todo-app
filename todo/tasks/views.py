from django.http import HttpResponseBadRequest
from django.views.generic import ListView
from django.shortcuts import redirect
from django.db.transaction import TransactionManagementError

from .models.collection import Collection


# Create your views here.
def process_add_collection(request):
    collection_name = request.POST["collection_name"]

    if collection_name == "":
        return HttpResponseBadRequest("A collection have to be named!")

    try:
        if request.method == "POST":
            collection = Collection(name=collection_name)
            collection.save()

    except TransactionManagementError as ex:
        print(f"Error while saving data to the db: {ex}")

    return redirect("index")


class RootView(ListView):
    model = Collection
    paginate_by = 2
    template_name = "index.html"
