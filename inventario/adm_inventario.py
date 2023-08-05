import requests
#Django
from django.db import transaction
from django.views.generic.edit import FormView
from django.views.generic import DetailView, TemplateView
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.urls import reverse
from django.views import View

class ViewSet(View):
    # User detail view
    initial = {'key': 'value'}
    template_name = 'administrador/viewproductos.html'
    def get(self, request, *args, **kwargs):
        context = {}
        context['action'] = action = self.kwargs['action']
        if not action:
            return render(request, template_name, context)
        if action == 'productos':
            try:
                context['title'] = 'Productos'
                # request['session'] = 1
                template_name = 'productos/viewproductos.html'
            except Exception as ex:
                return JsonResponse({"result": False, "mensaje": str(ex)})

        if action =='inicio':
            context['title']='Inicio'
            template_name = 'administrador/viewadministrador.html'
        return render(request, template_name, context)

    def post(self, request, *args, **kwargs):
        action = request.POST['action']
        with transaction.atomic():
            try:
                form = self.form_class(request.POST)
                if form.is_valid():
                    # <process form cleaned data>
                    return HttpResponseRedirect('/success/')
            except Exception as ex:
                transaction.set_rollback(True)
                return JsonResponse({"result": "bad", "mensaje": str(ex)})

        return render(request, self.template_name, {'form': form})