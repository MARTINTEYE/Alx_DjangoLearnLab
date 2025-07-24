from django import forms
from .models import Book

class BookSearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False)

from django import forms

class ExampleForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    email = forms.EmailField(label='Email')
    message = forms.CharField(widget=forms.Textarea, label='Message')
