from django.contrib import admin
from carts.admin import CartTabAdmin
from orders.admin import OrderTabulareAdmin

from users.models import User

# admin.site.register(User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "first_name", "last_name", "email", "phone_number"]
    search_fields = ["username", "first_name", "last_name", "email", "phone_number"]
    fields = ["username", "first_name", "last_name", "email", "phone_number", "delivery_address"]

    

    inlines = [CartTabAdmin, OrderTabulareAdmin]