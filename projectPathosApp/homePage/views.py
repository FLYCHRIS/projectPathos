from django.shortcuts import render

def home(request):
    return render(request, 'homePage/home.html', {'title': 'HOME'})

def plantAssist(request):
    return render(request, 'homePage/plantAssist.html', {'title': 'PLANT ASSIST'})
