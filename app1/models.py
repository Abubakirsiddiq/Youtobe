from django.contrib.auth.models import User
from django.db import models


class Account(models.Model):
    ism = models.CharField(max_length=50)
    email = models.EmailField()
    telefon = models.CharField(max_length=15)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Video(models.Model):
    nom = models.CharField(max_length=100)
    video = models.FileField()
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)


class Pleylist(models.Model):
    nom = models.CharField(max_length=100)
    videolar = models.ManyToManyField(Video)
    ochiq = models.BooleanField(default=True)


class Obuna(models.Model):
    obunalar = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, related_name="obunalar")
    obunachilar = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, related_name="obunachilar")


class Like(models.Model):
    video = models.ForeignKey(Video, on_delete=models.SET_NULL, null=True)
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)


class History(models.Model):
    nom = models.CharField(max_length=100)
    video = models.ForeignKey(Video, on_delete=models.SET_NULL, null=True)
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)

