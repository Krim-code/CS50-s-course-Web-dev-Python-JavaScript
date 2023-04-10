from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.

Json_output = {"1": {'text': "First page",
                     'img': "https://images.unsplash.com/photo-1679081194389-fd2a0f6e1d8e?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1632&q=80"}
    ,
               "2": {"text": "Second page",
                     "img": "https://images.unsplash.com/photo-1677226745336-8e04b6643142?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80"}
    ,
               "3": {"text": "Third page",
                     "img": "https://images.unsplash.com/photo-1679345506039-c4228a79c93a?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80"}}


def index(request):
    return render(request, "single/index.html")


def api(request, page):
    if str(page) in Json_output.keys():
        return JsonResponse(Json_output[str(page)], safe=True)
    else:
        return JsonResponse("Sorry, i don't have this page :(", safe=False)


def scroll(request):
    pass


def scroll_gen(request, page):
    array = []
    if page >= 1:
        array = {'pages': list(range(((page - 1) * 10) + 1, (page * 10) + 1))}
    elif page>=10:
        array = {'pages': list(range(page*page, (page*page) +10))}
    return JsonResponse(array, safe=True)
