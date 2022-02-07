from django.shortcuts import render, reverse, redirect
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    CreateView,
    FormView,
    DeleteView,
)
from . import models
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from . import forms


class HomeView(ListView):
    model = models.ListModel
    paginate_by = 10
    paginate_orphans = 4
    # ordering = "created"
    context_object_name = "lists"
    template_name = "lists/home.html"


class ListDetail(DetailView):

    model = models.ListModel
    context_object_name = "list"
    template_name = "lists/list.html"


class UpdateList(UpdateView):
    model = models.ListModel
    fields = (
        "title",
        "description",
        "host",
    )
    template_name = "lists/list_edit.html"


class CreateList(CreateView):
    model = models.ListModel
    form_class = forms.ListForm

    success_url = reverse_lazy("lists:home")
    template_name = "lists/listmodel_form.html"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class DeleteView(DeleteView):
    model = models.ListModel
    template_name = "lists/list.html"
    context_object_name = "list"

    def get_success_url(self):
        return reverse("lists:home")
