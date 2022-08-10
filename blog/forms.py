from dataclasses import fields
from django import forms

from . import models

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = '__all__'
        exclude = ['post']
        labels = {
            'user_name': 'Your name',
            'user_email': 'your email',
            'comment': 'your comment'
        }