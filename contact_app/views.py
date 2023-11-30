from django.shortcuts import render
from django.views.generic import CreateView
from .forms import ContactModelForm


# Create your views here.

class ContactView(CreateView):
    form_class = ContactModelForm
    template_name = 'contact_app/contact.html'
    success_url = '/contact-us/'

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data()
        context['url_page'] = "contact"
        return context