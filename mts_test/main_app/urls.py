from django.urls import path

from .views import ModelAView, ModelBView, ModelCView


app_name = "main_app"

urlpatterns = [
    path("modela/", ModelAView.as_view(), name="model_a"),
    path("modelb/", ModelBView.as_view(), name="model_b"),
    path("modelc/", ModelCView.as_view(), name="model_c"),
]
