from django import forms

class AddForm(forms.Form):
    name = forms.CharField(label="Pet Name")
    urls = forms.CharField(label="Image URLs (comma separated)", widget=forms.Textarea())