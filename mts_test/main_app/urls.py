from django.urls import path, include
from rest_framework import routers

from .views import ModelAList, ModelBList, ModelCList

app_name = 'main_app'

# router = routers.DefaultRouter()
# router.register("model_a", ModelAList, basename="model_a")
# router.register("model_b", ModelBList, basename="model_b")
# router.register("model_c", ModelCList, basename="model_c")

urlpatterns = [
    path("model_a/", ModelAList.as_view()),
    path("model_b/", ModelBList.as_view()),
    path("model_c/", ModelCList.as_view()),
]