from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from . import models


# Create your views here.
#authors
class AuthorList(PermissionRequiredMixin, generic.ListView):
    permission_required = ()
    model = models.Author


class AuthorDetail(PermissionRequiredMixin, generic.DetailView):
    permission_required = ()
    model = models.Author


class AuthorCreate(PermissionRequiredMixin, generic.CreateView):
    permission_required = "refs.add_author"
    model = models.Author
    fields = ['img', 'name', 'series', 'description']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Добавление нового автора'
        return context


class AuthorUpdate(PermissionRequiredMixin, generic.UpdateView):
    permission_required = "refs.change_author"
    model = models.Author
    fields = ['img', 'name', 'series', 'description']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["headline"] = 'Редактирование автора'
        return context


class AuthorDelete(PermissionRequiredMixin, generic.DeleteView):
    permission_required = "refs.delete_author"
    model = models.Author
    success_url = reverse_lazy("references:author-list")

#series
class SeriesList(PermissionRequiredMixin, generic.ListView):
    permission_required = ()
    model = models.Series


class SeriesDetail(PermissionRequiredMixin, generic.DetailView):
    permission_required = ()
    model = models.Series


class SeriesCreate(PermissionRequiredMixin, generic.CreateView):
    permission_required = ("refs.add_series")
    model = models.Series
    fields = ['name', 'description']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["headline"] = 'Добавление серии'
        return context


class SeriesUpdate(PermissionRequiredMixin, generic.UpdateView):
    permission_required = "refs.change_series"
    model = models.Series
    fields = ['name', 'description']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["headline"] = 'Редактирование серии'
        return context


class SeriesDelete(PermissionRequiredMixin, generic.DeleteView):
    permission_required = "refs.delete_series"
    model = models.Series
    success_url = reverse_lazy("references:series-list")

#Genre
class GenreList(PermissionRequiredMixin, generic.ListView):
    permission_required = ()
    model = models.Genre


class GenreDetail(PermissionRequiredMixin, generic.DetailView):
    permission_required = ()
    model = models.Genre


class GenreCreate(PermissionRequiredMixin, generic.CreateView):
    permission_required = ("refs.add_genre")
    model = models.Genre
    fields = ['name', 'description']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["headline"] = 'Добавление жанра'
        return context


class GenreUpdate(PermissionRequiredMixin, generic.UpdateView):
    permission_required = "refs.change_genre"
    model = models.Genre
    fields = ['name', 'description']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["headline"] = 'Редактирование жанра'
        return context


class GenreDelete(PermissionRequiredMixin, generic.DeleteView):
    permission_required = "goods.delete_genre"
    model = models.Genre
    success_url = reverse_lazy("references:genre-list")



#publishers
class PublisherList(PermissionRequiredMixin, generic.ListView):
    permission_required = ()
    model = models.Publisher


class PublisherDetail(PermissionRequiredMixin, generic.DetailView):
    permission_required = ()
    model = models.Publisher


class PublisherCreate(PermissionRequiredMixin, generic.CreateView):
    permission_required = ("refs.add_publisher")
    model = models.Publisher
    fields = ['name', 'description']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["headline"] = 'Добавление издательства'
        return context


class PublisherUpdate(PermissionRequiredMixin, generic.UpdateView):
    permission_required = "refs.change_publisher"
    model = models.Publisher
    fields = ['name', 'description']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["headline"] = 'Редактирование издательства'
        return context


class PublisherDelete(PermissionRequiredMixin, generic.DeleteView):
    permission_required = "refs.delete_publisher"
    model = models.Publisher
    success_url = reverse_lazy("references:publisher-list")
