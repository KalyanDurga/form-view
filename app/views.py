from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.views.generic import FormView,TemplateView

class CBV_form(FormView):
    template_name='CBV_form.html'
    form_class=StudentForm

    def form_valid(self, form):
        form.save()

        return HttpResponse('data submited')
