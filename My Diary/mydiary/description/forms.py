from dataclasses import field
from django import forms
from .models import Description,Comment

class PageForm(forms.ModelForm):
    #title=forms.CharField()
    #body=forms.CharField(widget=forms.Textarea)
    class Meta:
        model=Description
        fields='__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['content']