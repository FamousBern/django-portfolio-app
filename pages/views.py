from django.shortcuts import render
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.

def index(request):
    return render(request, 'index.html')

def sendmail(request):
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    from_email = request.POST.get('from_email', '')

    if subject and message and from_email:

        try:
            send_mail(subject, message, from_email, ['bernardberbell@gmail.com'])
            return HttpResponseRedirect('/index/')

        except:
            
            return HttpResponseRedirect('/index/')

    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')
