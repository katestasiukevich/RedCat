from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

# Create your models here.

user = get_user_model()
CODE_CHOICES = (
    ("25", "25"),
    ("29", "29"),
    ("33", "33"),
)


class CustomerProfile(models.Model):
    user = models.OneToOneField(user, related_name="profile", on_delete=models.CASCADE)
    first_name = models.CharField(verbose_name="Имя", max_length=100)
    last_name = models.CharField(verbose_name="Фамилия", max_length=100)
    email = models.EmailField(verbose_name="Email")
    code = models.CharField(
        verbose_name="Код мобильного оператора",
        max_length=2,
        choices=CODE_CHOICES,
        null=True,
        blank=True,
    )
    phone = models.CharField(
        verbose_name="Номер телефона", max_length=7, null=True, blank=True
    )
    country = models.CharField(
        verbose_name="Страна", max_length=100, null=True, blank=True
    )
    city = models.CharField(verbose_name="Город", max_length=100, null=True, blank=True)
    home_index = models.CharField(
        verbose_name="Почтовый индекс", max_length=7, null=True, blank=True
    )
    address1 = models.CharField(
        verbose_name="Адрес 1", max_length=100, null=True, blank=True
    )
    address2 = models.CharField(
        verbose_name="Адрес 2", max_length=100, null=True, blank=True
    )

    def get_absolute_url(self):
        return reverse_lazy("accounts:profile")

    def __str__(self):
        return f"Profile for user {self.user.username}"
