from django.shortcuts import render
from django.http import (
    HttpResponse,
    HttpResponseRedirect,
    Http404,
)
from django.urls import reverse


# Create your views here.
def home_page(request):
    return render(request, "blog/home_page.html")
