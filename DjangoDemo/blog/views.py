from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, JsonResponse, FileResponse
from django.shortcuts import render
from django.template import loader
from blog import models


def index(request):
    article = models.Aritcle.objects.get(pk=1)
    return render(request, 'blog/index.html', {'article':article})