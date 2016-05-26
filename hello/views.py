import os
import requests
import json

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
    #r = requests.post('http://104.236.75.160:4000'){'username':'<username here>','email':'<email here>','phone':'<phone # here>'} 
    #print r.text
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

            #TODO Remove for PROD
            token = ''
            
            try:
                r = requests.post('http://104.236.75.160:10000', json={'username':username, 'email':email, 'phone':phone})
                json_response = r.json()
                print (json_response['token'])
                token = json_response['token']
            except requests.exceptions.ConnectTimeout as e:
                print ("Signup connect timeout")
            except requests.exceptions.ReadTimeout as e:
                print ("Signup read timeout")
            except requests.exceptions.RequestException as e:
                print ("Signup request exception")
                
            #TODO For PROD environment
            #r = requests.post('http://twoefay.xyz:8080/register', json={'username':username, 'email':email, 'phone':phone})

            customer = Customer(username=username, password=password, email=email, phone=phone, token=token)
            customer.save()
            
            if token == '':
                return HttpResponse("Sign up successful but no twoefay")
                #return render(request, 'half_success.html')
            return HttpResponse("Sign up successful")
            #return render(request, 'success.html') 

    else:
        form = CustomerForm()
    
    return render(request, template, {'form':form})

#TODO Remove in PROD
def success(request):
    return render(request, 'success.html')

def login(request, template='login.html'):
    print('log in time!')
    form = LoginForm()
    if request.method == 'POST':
        print ('login form post')
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
                    #TODO ????
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

