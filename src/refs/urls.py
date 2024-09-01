from django.urls import path
from . import views


app_name = "references"
urlpatterns = [
    path('author-list/', views.AuthorList.as_view(), name="author-list"),
    path('author-detail/<int:pk>/', views.AuthorDetail.as_view(), name="author-detail"),
    path('author-create/', views.AuthorCreate.as_view(), name="author-create"),
    path('author-update/<int:pk>/', views.AuthorUpdate.as_view(), name="author-update"),
    path('author-delete/<int:pk>/', views.AuthorDelete.as_view(), name="author-delete"),

    path('series-list/', views.SeriesList.as_view(), name="series-list"),
    path('series-detail/<int:pk>/', views.SeriesDetail.as_view(), name="series-detail"),
    path('series-create/', views.SeriesCreate.as_view(), name="series-create"),
    path('series-update/<int:pk>/',views.SeriesUpdate.as_view(), name="series-update"),
    path('series-delete/<int:pk>/', views.SeriesDelete.as_view(), name="series-delete"),

    path('genre-list/', views.GenreList.as_view(), name="genre-list"),
    path('genre-detail/<int:pk>/', views.GenreDetail.as_view(), name="genre-detail"),
    path('genre-create/', views.GenreCreate.as_view(), name="genre-create"),
    path('genre-update/<int:pk>/', views.GenreUpdate.as_view(), name="genre-update"),
    path('genre-delete/<int:pk>/',views.GenreDelete.as_view(), name="genre-delete"),

    path('publisher-list/', views.PublisherList.as_view(), name="publisher-list"),
    path('publisher-detail/<int:pk>/', views.PublisherDetail.as_view(), name="publisher-detail"),
    path('publisher-create/', views.PublisherCreate.as_view(), name="publisher-create"),
    path('publisher-update/<int:pk>/', views.PublisherUpdate.as_view(), name="publisher-update"),
    path('publisher-delete/<int:pk>/', views.PublisherDelete.as_view(), name="publisher-delete"),
]
