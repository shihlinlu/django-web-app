from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.db.models import Q

from .forms import RestaurantCreateForm, RestaurantLocationCreateForm
from .models import RestaurantLocation

def restaurant_createview(request):
    form = RestaurantLocationCreateForm(request.POST or None)
    errors = None

    if form.is_valid():
        # customize
        # like a pre_save
        form.save()
        # like a post_save
        return HttpResponseRedirect("/restaurants/")
    if form.errors:
        errors = form.errors

    template_name = 'restaurants/form.html'
    context = {"form": form, "errors": errors}
    return render(request, template_name, context)

def restaurant_listview(request):
    template_name = 'restaurants/restaurantlocation_list.html'
    queryset = RestaurantLocation.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, template_name, context)

class RestaurantListView(ListView):
    def get_queryset(self):
        slug = self.kwargs.get("slug")
        if slug:
            queryset = RestaurantLocation.objects.filter(
                Q(category__iexact=slug) |
                Q(category__iexact=slug)
            )
        else:
            queryset = RestaurantLocation.objects.all()
        return queryset

class RestaurantDetailView(DetailView):
    queryset = RestaurantLocation.objects.all()

class RestaurantCreateView(CreateView):
    form_class = RestaurantLocationCreateForm
    template_name = 'restaurants/form.html'
    success_url = '/restaurants/'
