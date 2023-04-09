from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.

Json_output = {"1": "First page",
               "2": "Second page",
               "3": "Third page"}


def index(request):
    return render(request, "single/index.html")


def api(request, page):
    if str(page) in Json_output.keys():
        return JsonResponse(Json_output[str(page)],safe=False)
    else:
        return JsonResponse("Sorry, i don't have this page :(",safe=False)
