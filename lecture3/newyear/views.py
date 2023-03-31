import datetime

from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def index(request):
    data = datetime.datetime.now()
    return render(request,"newyear/index.html",
                  {
                      "newyear": data.month == 1 and data.day == 1
                      # "newyear": True
                  })
