from django.shortcuts import redirect, render
from django.views.generic import View
from django.http import HttpResponse, JsonResponse

class index(View):

    def get(self, request,  *args, **kwargs):
        template = 'index.html'

        return render(request, template, {})

class test(View):

    def get(self, request,  *args, **kwargs):


        return HttpResponse('Test success')
