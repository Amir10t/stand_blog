from django import forms
from .models import ContactModel

class ContactModelForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'id': 'name',
                'placeholder': 'your name'
            }),
            'email': forms.TextInput(attrs={
                'id': 'email',
                'placeholder':'your email'
            }),
            'subject': forms.TextInput(attrs={
                'id': 'subject',
                'placeholder': 'subject'
            }),
            'message': forms.Textarea(attrs={
                'rows': 5,
                'id': 'message',
                'placeholder':'your message'
            })
        }

        labels= {
            'name': '',
            'email': '',
            'subject':'',
            'message':''
        }
