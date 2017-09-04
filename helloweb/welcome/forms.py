from django import forms

class PostMessageForm(forms.Form):
    msg = forms.CharField(label="Leave a message", max_length=1024);
