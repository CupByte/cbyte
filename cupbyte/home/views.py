from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # render(request, 'index.html')
    # return HttpResponse("hello")
    return render(request, 'index.html')