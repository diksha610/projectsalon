from django.shortcuts import render
from .models import Emp
from django.core.mail import send_mail


# Create your views here.

def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        msg = request.POST['msg']
        date = request.POST['date']
        emp = Emp(name=name, email=email, phone=phone, msg=msg)
        emp.save()
        # SENDING MAIL
        host_mail = 'dikshak.1709@gmail.com'
        content = 'THE SALOON \n \n \n Customer name :'+name+'\n Customer email :'+email+'\n phone :'+phone+'\n Appointment For :'+msg
        send_mail('test mail', content, 'dikshak.1709@gmail.com', [email], fail_silently=False)
        send_mail('test mail', content, 'dikshak.1709@gmail.com', [host_mail], fail_silently=False)
        print('mail send successfulyy!!!')
    return render(request, 'index.html')
