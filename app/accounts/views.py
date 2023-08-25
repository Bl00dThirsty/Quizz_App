from django.shortcuts import render
from .models import Candidat




def signup(request, *args, **kwargs):

    if request.method == 'POST':
        name = request.POST['name']
        forename = request.POST['forename']
        date = request.POST['date']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        password = request.POST['password']
    #.signup != .create


        newCandidat = Candidat(name=name, forename=forename, date=date, email=email, phone_number=phone_number, password=password)
        newCandidat.save()


    return render(request, 'accounts/signup.html')
