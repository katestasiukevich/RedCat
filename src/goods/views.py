from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, render
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views import generic as generic_views

from goods.utils import q_search
#from acc import views
from . import models, forms

# Create your views here.
def catalog(request, category_slug=None):
    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)

    if category_slug == 'all':
        goods = models.Book.objects.all()
    elif query:
        goods = q_search(query)
    else:
        goods = get_list_or_404(models.Book.objects.filter(category__slug=category_slug))
    
    if on_sale:
        goods = goods.filter(discount__gt=0)
    if order_by and order_by != "default":
        goods = goods.order_by(order_by)
    
    paginator = Paginator(goods, 9)
    current_page = paginator.page(int(page))
    context = {
        'title': 'RED CAT - Каталог',
        'goods': current_page,
        'slug_url': category_slug,
    }
    return render(request, 'goods/catalog.html', context=context)

def product(request):
    return render(request, 'goods/product.html')

class BookList(generic_views.ListView):
    #permission_required = ()
    login_url = reverse_lazy("accounts:login")
    model = models.Book


class BookCreate(generic_views.CreateView):
    #permission_required = "goods.add_book"
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


class BookDetail(generic_views.DetailView):
    #permission_required = ()
    model = models.Book


class BookUpdate(generic_views.UpdateView):
    #permission_required = "goods.change_book"
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


class BookDelete(generic_views.DeleteView):
    #permission_required = "goods.delete_book"
    model = models.Book
    success_url = reverse_lazy("goods:book-list")
