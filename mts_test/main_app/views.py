from typing import Any

from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .models import ModelA, ModelB, ModelC


class ContextQuerysetMixin:
    fields = "__all__"
    context_object_name = "model_data"
    template_name = "main_app/models_form.html"
    paginate_by = 2
    fields_order = tuple()  # порядок вывода столбцов

    def get_queryset(self) -> QuerySet:
        queryset = super().get_queryset()
        return queryset.values(*self.fields_order)[:20]

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["columns"] = self.fields_order
        context["table"] = self.model.__name__
        return context


class ModelAView(ContextQuerysetMixin, CreateView, ListView):
    success_url = reverse_lazy("main_app:model_a")
    model = ModelA
    fields_order = ("id", "a_one", "a_two", "a_three")


class ModelBView(ContextQuerysetMixin, CreateView, ListView):
    success_url = reverse_lazy("main_app:model_b")
    model = ModelB
    fields_order = ("id", "b_two", "b_three", "b_one")


class ModelCView(ContextQuerysetMixin, CreateView, ListView):
    success_url = reverse_lazy("main_app:model_c")
    model = ModelC
    fields_order = ("id", "c_three", "c_one", "c_two")
