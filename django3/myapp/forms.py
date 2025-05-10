from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=40)
    email = forms.EmailField(label='Email', max_length=40)
    message = forms.CharField(label='Message', max_length=200, widget=forms.Textarea)