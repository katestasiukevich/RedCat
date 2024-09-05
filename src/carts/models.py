from django.db import models
from goods.models import Book

from users.models import User

# Create your models here.
class CartQueryset(models.QuerySet):
    
    def total_price(self):
        return sum(cart.books_price() for cart in self)
    
    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class Cart(models.Model):

    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Пользователь')
    book = models.ForeignKey(to=Book, on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Количество')
    session_key = models.CharField(max_length=32, null=True, blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    class Meta:
        db_table = 'cart'
        verbose_name = "Корзина"
        verbose_name_plural = "Корзина"
        ordering = ("id",)

    objects = CartQueryset().as_manager()

    def books_price(self):
        return round(self.book.sell_price() * self.quantity, 2)


    def __str__(self):
        if self.user:
            return f'Корзина {self.user.username} | Товар {self.book.title} | Количество {self.quantity}'
            
        return f'Анонимная корзина | Товар {self.book.title} | Количество {self.quantity}'