from django.contrib import admin
from .models import Series, Author, Publisher, Genre
# Register your models here.
admin.site.register(Series)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Genre)