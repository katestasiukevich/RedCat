from django.urls import path
from . import views

app_name = "goods"
urlpatterns = [
    path('', views.catalog, name="index"),
    path('product/', views.product, name="product"),
    path('book-list/', views.BookList.as_view(), name="book-list"),
    path('book-create/', views.BookCreate.as_view(), name="book-create"),
    path('book-detail/<int:pk>/', views.BookDetail.as_view(), name="book-detail"),
    path('book-update/<int:pk>/', views.BookUpdate.as_view(), name="book-update"),
    path('book-delete/<int:pk>/', views.BookDelete.as_view(), name="book-delete"),
]
