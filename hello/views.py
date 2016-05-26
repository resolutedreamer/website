import os
import requests

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.conf import settings
from django.core.urlresolvers import reverse

from .forms import CustomerForm
from .forms import LoginForm
from .models import Customer

def index(request):
    #return HttpResponse('Hello from Python!')
    return render(request, 'index.html')
    #r = requests.get('https://lh6.ggpht.com/8R2VbnmJNqIHQZDB9gJ5FgnYlFcUO1c14BRQT2yahNKIDo1AXryjqX2waWt2cU-GPw=w300')
    #print r.text
    #return HttpResponse('<pre>' + r.text + '</pre>')

    #times = int(os.environ.get('TIMES',3))
    #return HttpResponse('Hello! ' * times)

def customer_new (request, template='customer_new.html'):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            if username:
                print('cleaned username:' + username)
            else:
                print('no username')
            password = form.cleaned_data.get('password')
            if password:
                print('cleaned password: ' + password)
            else:
                print('no password')
            email = form.cleaned_data.get('email')
            if email:
                print('cleaned email: ' + email)
            else:
                print('no email')
            phone = form.cleaned_data.get('phone')
            if phone:
                print('cleaned phone: ' + phone)
            else:
                print('no phone')

            customer = Customer(username=username, password=password, email=email, phone=phone)
            customer.save()

            #return HttpResponseRedirect('success.html')
            return render(request, 'success.html') 

    else:
        form = CustomerForm()
    
    return render(request, template, {'form':form})

def success(request):
    return render(request, 'success.html')

def login(request, template='login.html'):
    print('log in time!')
    form = LoginForm()
    if request.method == 'POST':
        print ('checking post')
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            if username:
                print('cleaned username:' + username)
            else:
                print('no username')
            password = form.cleaned_data.get('password')
            if password:
                print('cleaned password: ' + password)
            else:
                print('no password')
    
            try:
                customer = Customer.objects.get(username=username)
            except Customer.DoesNotExist:
                customer = None

            if customer == None:
                return HttpResponse('username does not exist. please go sign up for an account')
            else:
                if password == customer.password:
                    return HttpResponseRedirect('success.html')
                else:
                    return HttpResponse('password is incorrect!')
        else: 
            form = LoginForm()
    return render(request, template, {'form':form})

#def db(request):

#    greeting = Greeting()
#    greeting.save()

#    greetings = Greeting.objects.all()

#    return render(request, 'db.html', {'greetings': greetings})

