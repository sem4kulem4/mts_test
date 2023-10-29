from django.db import models


class ModelA(models.Model):
    a_one = models.CharField(max_length=200)
    a_two = models.CharField(max_length=200)
    a_three = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"{self.a_one} - {self.a_two} - {self.a_three}"


class ModelB(models.Model):
    b_one = models.CharField(max_length=200)
    b_two = models.CharField(max_length=200)
    b_three = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"{self.b_one} - {self.b_two} - {self.b_three}"


class ModelC(models.Model):
    c_one = models.CharField(max_length=200)
    c_two = models.CharField(max_length=200)
    c_three = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"{self.c_one} - {self.c_two} - {self.c_three}"
