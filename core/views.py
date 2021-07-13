from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from core.models import Contact


def base(request):
    return render(request, 'base.html')


def contactview(request):
    if request.POST:
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact()
        contact.name = name
        contact.email = email
        contact.message = message
        contact.save()
        messages.info(request, 'Thankyou!! your feedback been has received ')
    return render(request, 'contact.html')


def adminview(request):
    contact = Contact.objects.all()
    return render(request, 'admin.html', {'contact': contact})


def delete(request, contact_id):
    contact = Contact.objects.get(pk=contact_id)
    contact.delete()
    messages.success(request, 'item has been successfully deleted!')
    return redirect('adminview')


def loginview(request):
    if request.method == 'POST':
        user = User()
        Username = request.POST['Username']
        password = request.POST['password']
        user.username = Username
        user.password = password
        user = authenticate(request, username=Username, password=password)
        if user is not None:
            login(request, user)
            return redirect('adminview')
        if user is None:
            return HttpResponse("you are not authorised to access this page!!!")
    else:

        return render(request, 'login.html')
