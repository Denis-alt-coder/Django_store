from django.shortcuts import render


def index(request):
    return render(request, 'main/shop.html')


def cart(request):
    return render(request, 'main/cart.html')
