from django.shortcuts import render
from website.models import Contact, Newsletter
from website.forms import  ContactForm , NewsletterForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

# def maintenance(request):
#     return render(request, 'maintenance.html')

def home_view(request):
    return render(request, 'website/index.html')

def about_view(request):
    return render(request, 'website/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            new = form.save(commit=False)
            new.name = "Unknown"
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your Ticket Successfully Sent.')
        else:
            messages.add_message(request, messages.ERROR, 'Something Went Wrong !!! ')

    else:
        form = ContactForm()

    return render(request, 'website/contact.html', {'form':form})

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
      
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your Email Successfully Submited.', extra_tags='alert')

        else:
            messages.add_message(request, messages.ERROR, 'Something Went Wrong !!! ', extra_tags='alert')

    else:
        form = NewsletterForm()

    return HttpResponseRedirect('/')

def test(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Successfully Sent.')
  
            return HttpResponseRedirect('test')

        else:
            messages.add_message(request, messages.ERROR, 'Something Wrong !!! ')
            return HttpResponse('<p>not valid</p>')

    else:
        form = ContactForm()

    return render(request, 'website/test.html', {'form':form})