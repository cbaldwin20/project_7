from django.shortcuts import render


def home(request):
    """home page"""
    return render(request, 'home.html')
    