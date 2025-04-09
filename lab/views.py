from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return render(request,'home.html', {'user': request.user})
    # return HttpResponse("Hello, world. You're at the polls index.")
