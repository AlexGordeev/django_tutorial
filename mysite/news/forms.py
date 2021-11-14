from django import forms

from .models import Category


class NewsForm(forms.Form):
    title = forms.CharField(label='Название', max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label='Содержимое', required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    is_published = forms.BooleanField(initial=True, label='Опубликовано')
    category = forms.ModelChoiceField(empty_label='Выберите категорию', label='Категория', queryset=Category.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
