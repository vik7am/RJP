from django.shortcuts import render


def index_view(request):
    if request.method == "GET":
        return render(request, "index.html", {})


def index_view_2(request):
    if request.method == "GET":
        return render(request, "index.html", {})


def about_view(request):
    if request.method == "GET":
        return render(request, "about-us.html", {})
