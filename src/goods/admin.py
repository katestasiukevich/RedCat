from django.contrib import admin

from goods.models import Categories, Book

# admin.site.register(Categories)
# admin.site.register(Products)


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name",]

@admin.register(Book)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ["title", "quantity", "price", "discount"]
    list_editable = ["discount",]
    search_fields = ["title", "description"]
    list_filter = ["discount", "quantity", "category"]
    fields = [
        "title",
        "category",
        "slug",
        "description",
        "cover",
        ("price", "discount"),
        "quantity",
    ]
