from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from . import models


# Create your views here.
#authors
class AuthorList(generic.ListView):
    #permission_required = ()
    model = models.Author


class AuthorDetail(generic.DetailView):
    #permission_required = ()
    model = models.Author


class AuthorCreate(generic.CreateView):
    #permission_required = "refs.add_author"
    model = models.Author
    fields = ['img', 'name', 'series', 'description']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Добавление нового автора'
        return context


class AuthorUpdate(generic.UpdateView):
    #permission_required = "refs.change_author"
    model = models.Author
    fields = ['img', 'name', 'series', 'description']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["headline"] = 'Редактирование автора'
        return context


class AuthorDelete(generic.DeleteView):
    #permission_required = "refs.delete_author"
    model = models.Author
    success_url = reverse_lazy("references:author-list")

#series
class SeriesList(generic.ListView):
    #permission_required = ()
    model = models.Series


class SeriesDetail(generic.DetailView):
    #permission_required = ()
    model = models.Series


class SeriesCreate(generic.CreateView):
    #permission_required = ("refs.add_series")
    model = models.Series
    fields = ['name', 'description']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["headline"] = 'Добавление серии'
        return context


class SeriesUpdate(generic.UpdateView):
    #permission_required = "refs.change_series"
    model = models.Series
    fields = ['name', 'description']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["headline"] = 'Редактирование серии'
        return context


class SeriesDelete(generic.DeleteView):
    #permission_required = "refs.delete_series"
    model = models.Series
    success_url = reverse_lazy("references:series-list")

#Genre
class GenreList(generic.ListView):
    #permission_required = ()
    model = models.Genre


class GenreDetail(generic.DetailView):
    #permission_required = ()
    model = models.Genre


class GenreCreate(generic.CreateView):
    #permission_required = ("refs.add_genre")
    model = models.Genre
    fields = ['name', 'description']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["headline"] = 'Добавление жанра'
        return context


class GenreUpdate(generic.UpdateView):
    #permission_required = "refs.change_genre"
    model = models.Genre
    fields = ['name', 'description']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["headline"] = 'Редактирование жанра'
        return context


class GenreDelete(generic.DeleteView):
    #permission_required = "goods.delete_genre"
    model = models.Genre
    success_url = reverse_lazy("references:genre-list")



#publishers
class PublisherList(generic.ListView):
    #permission_required = ()
    model = models.Publisher


class PublisherDetail(generic.DetailView):
    #permission_required = ()
    model = models.Publisher


class PublisherCreate(generic.CreateView):
    #permission_required = ("refs.add_publisher")
    model = models.Publisher
    fields = ['name', 'description']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["headline"] = 'Добавление издательства'
        return context


class PublisherUpdate(generic.UpdateView):
    #permission_required = "refs.change_publisher"
    model = models.Publisher
    fields = ['name', 'description']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["headline"] = 'Редактирование издательства'
        return context


class PublisherDelete(generic.DeleteView):
    #permission_required = "refs.delete_publisher"
    model = models.Publisher
    success_url = reverse_lazy("references:publisher-list")
