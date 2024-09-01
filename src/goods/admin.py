from django.contrib import admin
from .models import Categories, Book


# Register your models here.
#admin.site.register(Categories)
@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
