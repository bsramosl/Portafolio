from django.shortcuts import render, redirect , get_object_or_404
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView, RedirectView,DetailView
from PrincipalApp.forms import *
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.db import transaction
from django.http import HttpResponseRedirect, request, HttpResponse, JsonResponse
import json , random
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import login, logout, update_session_auth_hash,authenticate
from django.views.decorators.cache import never_cache
from django.views.generic.edit import FormView
from django.core.exceptions import *
from django.http import Http404
from django.core.mail import send_mail



class Index(TemplateView):
    template_name = 'Index.html'

class About(TemplateView):
    template_name = 'About.html'
  
def Contact(request):
    # CONTACT FORM
    if request.method == 'POST':
        name = request.POST.get('full-name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        form_data = {
            'name':name,
            'email':email,
            'subject':subject,
            'message':message,
        }
        message = '''
        From:\n\t\t{}\n
        Message:\n\t\t{}\n
        Email:\n\t\t{}\n
        subject:\n\t\t{}\n
        '''.format(form_data['name'], form_data['message'], form_data['email'],form_data['subject'])
        send_mail('You got a mail!', message, '', ['steeven10f@gmail.com']) # TODO: enter your email address
        
    return render(request, 'Contact.html', {})