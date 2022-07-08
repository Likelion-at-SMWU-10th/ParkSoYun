from django import forms

class PageForm(forms.Form):
    title=forms.CharField()
    body=forms.CharField(widget=forms.Textarea)
