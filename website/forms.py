# from django import forms
from django.forms import ModelForm
from website.models import Contact, Newsletter


# class NameForm(forms.Form):
#     name = forms.CharField(label='name',max_length=255)
#     email = forms.EmailField(label='email')
#     subject = forms.CharField(label='subject',max_length=255)
#     message = forms.CharField(label='message', widget=forms.Textarea)

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        # exclude = ['name']

class NewsletterForm(ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'