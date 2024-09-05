from django.contrib import admin

from carts.models import Cart

# admin.site.register(Cart)
class CartTabAdmin(admin.TabularInline):
    model = Cart
    fields = "book", "quantity", "created_timestamp"
    search_fields = "book", "quantity", "created_timestamp"
    readonly_fields = ("created_timestamp",)
    extra = 1


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ["user_display", "book_display", "quantity", "created_timestamp",]
    list_filter = ["created_timestamp", "user", "book__title",]

    def user_display(self, obj):
        if obj.user:
            return str(obj.user)
        return "Анонимный пользователь"

    def book_display(self, obj):
        return str(obj.book.title)

    # user_display and product_display alter name of columns in admin panel
    user_display.short_description = "Пользователь"
    book_display.short_description = "Товар"




    