from django.shortcuts import render
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views import generic as generic_views
#from acc import views
from . import models, forms

# Create your views here.
def catalog(request):
    goods = models.Book.objects.all()
    context = {
        'title': 'RED CAT - Каталог',
        'goods': goods
    }
    return render(request, 'goods/catalog.html', context=context)

def product(request):
    return render(request, 'goods/product.html')

class BookList(PermissionRequiredMixin, generic_views.ListView):
    permission_required = ()
    login_url = reverse_lazy("accounts:login")
    model = models.Book


class BookCreate(PermissionRequiredMixin, generic_views.CreateView):
    permission_required = "goods.add_book"
    model = models.Book
    login_url = reverse_lazy("accounts:login")
    success_url = reverse_lazy("accounts:profile")
    fields = [
        "category",
        "title",
        "author",
        "series",
        "genre",
        "publisher",
        "cover",
        "description",
        "price",
        "discount",
        "quantity",
        "year",
        "pages",
        "binding",
        "book_format",
        "isbn",
        "weight",
        "age_restrictions",
        "stock",
        "available"
    ]
    form = forms.BookCreateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["headline"] = 'Добавление нового товара "Книга"'
        return context


class BookDetail(PermissionRequiredMixin, generic_views.DetailView):
    permission_required = ()
    model = models.Book


class BookUpdate(PermissionRequiredMixin, generic_views.UpdateView):
    permission_required = "goods.change_book"
    model = models.Book
    fields = [
        "category",
        "title",
        "author",
        "series",
        "genre",
        "publisher",
        "cover",
        "description",
        "price",
        "discount",
        "quantity",
        "year",
        "pages",
        "binding",
        "book_format",
        "isbn",
        "weight",
        "age_restrictions",
        "stock",
        "available"
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["headline"] = 'Редактирование товара "Книга"'
        return context


class BookDelete(PermissionRequiredMixin, generic_views.DeleteView):
    permission_required = "goods.delete_book"
    model = models.Book
    success_url = reverse_lazy("goods:book-list")
