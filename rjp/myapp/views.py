from django.shortcuts import render


def index_view(request):
    if request.method == "GET":
        return render(request, "index.html", {})


def index_view_2(request):
    if request.method == "GET":
        return render(request, "index.html", {})


def index_2_view(request):
    if request.method == "GET":
        return render(request, "index2.html", {})


def index_3_view(request):
    if request.method == "GET":
        return render(request, "index3.html", {})


def index_4_view(request):
    if request.method == "GET":
        return render(request, "index4.html", {})


def about_view(request):
    if request.method == "GET":
        return render(request, "about-us.html", {})
