import os
import requests

from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from .models import Greeting
from .forms import SubscriberForm
from .models import Subscriber

# Create your views here.

def index(request):
    #return HttpResponse('Hello from Python!')
    return render(request, 'index.html')
    #r = requests.get('https://lh6.ggpht.com/8R2VbnmJNqIHQZDB9gJ5FgnYlFcUO1c14BRQT2yahNKIDo1AXryjqX2waWt2cU-GPw=w300')
    #print r.text
    #return HttpResponse('<pre>' + r.text + '</pre>')

    #times = int(os.environ.get('TIMES',3))
    #return HttpResponse('Hello! ' * times)

def subscriber_new (request, template='subscriber_new.html'):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']

            user = User(username = username, email = email, first_name = first_name, last_name = last_name)
            user.set_password(password)
            user.save()

            address_one = form.cleaned_data['address_one']
            address_two = form.cleaned_data['address_two']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            sub = Subscriber(address_one = address_one, address_two = address_two, city=city, state=state, user_rec=user)
            sub.save()

            return HttpResponseRedirect('/success/')
    else:
        form = SubscriberForm()
    return render(request, template, {'form':form})

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

