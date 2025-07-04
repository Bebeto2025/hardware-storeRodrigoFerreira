from django import forms
from django.contrib.auth.models import User
from .models import Message

class MessageForm(forms.ModelForm):
    recipient = forms.ModelChoiceField(
        queryset=User.objects.all(),
        label="Para",
        widget=forms.Select(attrs={"class": "form-control"})
    )

    class Meta:
        model = Message
        fields = ["recipient", "content"]
        widgets = {
            "content": forms.Textarea(attrs={"rows": 4, "class": "form-control"}),
        }
