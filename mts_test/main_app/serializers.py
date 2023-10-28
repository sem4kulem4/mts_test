from rest_framework import serializers

from .models import ModelA, ModelB, ModelC


class ModelASerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelA
        fields = ("a_one", "a_two", "a_three")

class ModelBSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelB
        fields = ("b_one", "b_two", "b_three")

class ModelCSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelC
        fields = ("c_one", "c_two", "c_three")
