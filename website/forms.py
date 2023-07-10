from django.forms import ModelForm
from website.models import Contact, Newsletter
from captcha.fields import CaptchaField


class ContactForm(ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Contact
        fields = '__all__'
        # exclude = ['name']

class NewsletterForm(ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'