from django.shortcuts import render
from django.http import HttpRequest


def starting_page(request: HttpRequest):
    return render(request, "blog/index.html")


def posts(request: HttpRequest):
    pass


def post_detail(request: HttpRequest):
    pass
