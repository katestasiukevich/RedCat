from django import forms
from django.contrib.auth.models import User
from . import models
from .models import CustomerProfile

CODE_CHOICES = {
    ("25", "25"),
    ("29", "29"),
    ("33", "33"),
}


class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = models.CustomerProfile
        template_name = "acc/profile-form.html"
        fields = [
            "first_name",
            "last_name",
            "code",
            "phone",
            "country",
            "city",
            "home_index",
            "address1",
            "address2",
        ]


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("Passwords don't match.")
        return cd["password2"]


# class UserEditForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ("first_name", "last_name", "email")


# class ProfileEditForm(forms.ModelForm):
#     class Meta:
#         model = CustomerProfile
#         fields = (
#             "code",
#             "phone",
#             "country",
#             "city",
#             "home_index",
#             "address1",
#             "address2",
#         )
