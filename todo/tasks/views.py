from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseBadRequest


# Create your views here.
def add_collection_view(request):
    if request.method == "POST":
        collection_name = request.POST["collection_name"]

        if collection_name == "":
            return HttpResponseBadRequest("A collection have to be named!")

    print("process_form")
    return HttpResponse("ok")


class RootView(TemplateView):
    template_name = "index.html"
    context = {"username": "kevin"}
