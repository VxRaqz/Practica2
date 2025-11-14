from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "addon1/home.html")
    