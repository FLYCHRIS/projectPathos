from django.shortcuts import render

def PAMenu(request):
    return render(request, 'menuPage/plantAssist.html', {'title': 'PLANT ASSIST'})
