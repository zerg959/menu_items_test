from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def team(request):
    return render(request, 'team.html')

def page3(request):
    return render(request, 'page3.html')

def contacts(request):
    return render(request, 'contacts.html')