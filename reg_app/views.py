from django.shortcuts import render
from .models import *
from django.core.mail import send_mail
from django.conf import settings
from random import randrange

# Create your views here.

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        # error aavse eno meaning evo chhe ke DB ma aa email chhe j nahi
        try:
            u_obj = User.objects.get(email = request.POST['email'])
            return render(request, 'register.html', {'msg': 'Email is Already Register !!'})
        except:
            if request.POST['password'] == request.POST['repassword']:
                global c_otp, f
                f = request.POST['full_name']
                e = request.POST['email']
                p = request.POST['password']
                c_otp = randrange(1000000, 999999, -1)
                send_mail(
                    'Welcome', 
                    f'your OTP is 1234{c_otp}', 
                    settings.EMAIL_HOST_USER,
                    [request.POST['email']])
                return render(request, 'otp.html')    
            else :
                return render(request, 'register.html', {'msg' : 'Both password Do not Match'}) 




def otp_function(request):
    if str(c_otp) == request.POST['ooty']:
        User.objects.create(
            full_name = f,
            email = e,
            password = p
        )
        return render(request, 'register.html', {'msg': ' Successfully Registered !!'})
    else:
        return render(request, 'otp.html', {'k': 'Wrong OTP !!'})