from django import forms
from .models import Article
from django.db import models
class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')

class NewsLetterrecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()

class NewArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ['editor', 'pub_date']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }        