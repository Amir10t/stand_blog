from django import forms
from .models import CommentPostModel

# class CommentPostModelForm(forms.ModelForm):
#     class Meta():
#         model = CommentPostModel
#         fields = ('name', 'email', 'message')
#
class CommentForm(forms.Form):
    name = forms.CharField(
        label='',
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'name',
            'placeholder': 'Your Name'
        })
    )
    email = forms.EmailField(
        label='',
        widget=forms.EmailInput(attrs={
            'class': 'email',
            'placeholder': 'Email'
        })
    )
    message = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'class': 'message',
            'placeholder': 'Your Message',
            'rows': '5',
            'id': 'message'
        })
    )