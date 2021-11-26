from django import forms
from django.forms import widgets

class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Your Name"
            }
        )
    )
    body = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Leave a comment"
            }
        )
    )