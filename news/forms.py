from .models import Articl
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticlForm(ModelForm):
    class Meta:
        model = Articl
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи',
            }),

            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи',
            }),

            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата',
            }),

            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи',
            }),
        }
