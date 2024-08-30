from django import forms

class ContactForm(forms.Form):
    name = forms.CharField( max_length=100, min_length=1, required=True, label="Введите ваше имя")
    message = forms.CharField(required=True, label="Оставьте ваше сообщение", widget=forms.Textarea)
