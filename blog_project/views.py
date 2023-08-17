from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='home.html',
        context=contexto,
    )
    return http_response