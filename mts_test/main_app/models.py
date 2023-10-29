from django.db import models


class ModelA(models.Model):
    class Meta:
        ordering = ["id"]

    a_one = models.CharField(max_length=200, blank=True)
    a_two = models.CharField(max_length=200, blank=True)
    a_three = models.CharField(max_length=200, blank=True)

    def __str__(self) -> str:
        return f"{self.a_one} - {self.a_two} - {self.a_three}"


class ModelB(models.Model):
    class Meta:
        ordering = ["id"]

    b_one = models.CharField(max_length=200, blank=True)
    b_two = models.CharField(max_length=200, blank=True)
    b_three = models.CharField(max_length=200, blank=True)

    def __str__(self) -> str:
        return f"{self.b_one} - {self.b_two} - {self.b_three}"


class ModelC(models.Model):
    class Meta:
        ordering = ["id"]

    c_one = models.CharField(max_length=200, blank=True)
    c_two = models.CharField(max_length=200, blank=True)
    c_three = models.CharField(max_length=200, blank=True)

    def __str__(self) -> str:
        return f"{self.c_one} - {self.c_two} - {self.c_three}"
