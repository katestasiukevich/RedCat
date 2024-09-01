from django.db import models
from django.urls import reverse_lazy
from refs.models import Author, Series, Publisher, Genre

# Create your models here.
class Categories(models.Model):
    name = models.CharField(verbose_name="Название", max_length=100, db_index=True)
    slug = models.SlugField(verbose_name="URL", max_length=200, db_index=True)

    class Meta:
        ordering = ('name', )
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return f"{self.name}"
    
RESTRICTION_CHOICES = (
    ("0+", "0+"),
    ("6+", "6+"),
    ("12+", "12+"),
    ("16+", "16+"),
    ("18+", "18+"),
)

class Book(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.PROTECT, related_name='products', verbose_name="Категория")
    title = models.CharField(
        verbose_name="Название книги", max_length=200, auto_created=False, db_index=True
    )
    slug = models.SlugField(verbose_name="URL", max_length=200, db_index=True)
    cover = models.ImageField(verbose_name="Обложка", upload_to="book_covers/%Y/%m/%d/", blank=True, null=True)
    # author_id = Author.objects.get(pk=1)
    author = models.ManyToManyField(
        Author, related_name="author", verbose_name="Автор"
    )  # , default=author_id)
    series = models.ForeignKey(
        Series, on_delete=models.PROTECT, related_name="series", verbose_name="Серия"
    )
    genre = models.ManyToManyField(Genre, related_name="genre", verbose_name="Жанр")
    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.PROTECT,
        related_name="publisher",
        verbose_name="Издательство",
        null=True,
        blank=True,
    )
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    price = models.DecimalField(verbose_name="Цена", decimal_places=2, max_digits=7, default=0.00)
    discount = models.DecimalField(verbose_name="Скидка в %", decimal_places=2, max_digits=7, default=0.00)
    quantity = models.PositiveIntegerField(verbose_name="Количество", default=0)
    year = models.PositiveSmallIntegerField(verbose_name="Год издания", blank=True, null=True)
    pages = models.PositiveSmallIntegerField(verbose_name="Страниц")
    binding = models.CharField(verbose_name="Переплёт", max_length=100)
    book_format = models.CharField(verbose_name="Формат", max_length=100, blank=True, null=True)
    isbn = models.CharField(verbose_name="ISBN", max_length=100)
    weight = models.IntegerField(verbose_name="Вес (гр)", blank=True, null=True)
    age_restrictions = models.CharField(
        verbose_name="Возрастные ограничения",
        max_length=3,
        choices=RESTRICTION_CHOICES,
        null=True,
        blank=True,
    )
    created = models.DateTimeField(
        verbose_name="Дата внесения в каталог", auto_now_add=True, auto_now=False, blank=True, null=True
    )
    updated = models.DateTimeField(
        verbose_name="Дата последнего изменения карточки", auto_now_add=False, auto_now=True, blank=True, null=True 
    )
    stock = models.PositiveIntegerField(verbose_name="Остаток")
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ('title',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return f"{self.title} количество - {self.quantity}"

    def get_absolute_url(self):
        return reverse_lazy("goods:book-detail", kwargs={"pk": self.pk})
    
    def display_id(self):
        return f"{self.pk:05}"
    
    def sell_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2)
        return self.price

    