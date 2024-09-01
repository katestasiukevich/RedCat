from django.db import models
from django.urls import reverse_lazy


# Create your models here.
class Series(models.Model):
    """class for series references"""

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse_lazy("references:series-detail", kwargs={"pk": self.pk})


class Author(models.Model):
    """class for author references"""

    name = models.CharField(max_length=100)
    series = models.ForeignKey(Series, on_delete=models.PROTECT, related_name="authors")
    description = models.TextField(blank=True, null=True)
    img = models.ImageField(
        null=True,
        blank=True,
        verbose_name="Фото/портрет автора",
        upload_to="author_img/",
    )

    def __str__(self) -> str:
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse_lazy("references:author-detail", kwargs={"pk": self.pk})
    
class Genre(models.Model):
    """class for genre references"""

    name = models.CharField(verbose_name="Название", max_length=100, unique=True)
    slug = models.SlugField(verbose_name="URL", max_length=200, unique=True, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def get_absolute_url(self):
        return reverse_lazy("references:genre-detail", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return f"{self.name}"




class Publisher(models.Model):
    """class for publisher references"""

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse_lazy("references:publisher-detail", kwargs={"pk": self.pk})
