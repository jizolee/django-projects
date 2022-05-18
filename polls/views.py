from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. 6e66b465 is the polls index.")