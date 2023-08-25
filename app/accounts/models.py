from django.db import models
from django import forms
from django.forms import PasswordInput
import os

class Candidat(models.Model):

    name = models.CharField(max_length=100)
    forename = models.CharField(max_length=100)
    date = models.DateField()
    email = models.EmailField()
    phone_number = models.IntegerField()
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)
    actif = models.BooleanField(default=True)


    class Meta: 
        verbose_name = ("Candidat")
        verbose_name_plural = ("Candidats")
    

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise models.ValidationError("Les mots de passe ne correspondent pas.")

            def __str__(self):
                return self.name
                #return f"{self.name} ({self.stock})"