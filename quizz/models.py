from django.db import models
from django import forms
# Create your models here.


"""
******************************************* Planification du modèle *****************************************************
FORMULAIRE D'INSCRIPTION


- nom
- prenom
- date de naissance
- email
- numero de téléphone

FORMULAIRE DE RECONNEXION

- code de révaluation

"""



class RegistrationForm(forms.Form):
    name = forms.CharField(label='Nom du candidat', max_length=100)
    forename = forms.CharField(label='Prenom du candidat', max_length=100)
    email = forms.EmailField(label='Adresse e-mail')
    phone_number = forms.IntegerField()
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirmez le mot de passe', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Les mots de passe ne correspondent pas.")