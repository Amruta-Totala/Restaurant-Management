from django.shortcuts import render


def home(request):
    return render(request, "home.html", {})


def about(request):
    return render(request, "about.html", {})


def feature(request):
    return render(request, "feature.html", {})


def contact(request):
    return render(request, "contact.html", {})


def team(request):
    return render(request, "team.html", {})


def menu(request):
    return render(request, "menu.html", {})


def booking(request):
    return render(request, "booking.html", {})
