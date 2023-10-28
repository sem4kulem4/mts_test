from django.db import models


class ModelA(models.Model):
    a_one = models.CharField(max_length=200)
    a_two = models.CharField(max_length=200)
    a_three = models.CharField(max_length=200)


class ModelB(models.Model):
    b_one = models.CharField(max_length=200)
    b_two = models.CharField(max_length=200)
    b_three = models.CharField(max_length=200)


class ModelC(models.Model):
    c_one = models.CharField(max_length=200)
    c_two = models.CharField(max_length=200)
    c_three = models.CharField(max_length=200)