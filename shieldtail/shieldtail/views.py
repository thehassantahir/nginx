from django.http import HttpResponse

def index(request):
    return HttpResponse("This is a connection repo of NGINX WSGI with DJANGO")