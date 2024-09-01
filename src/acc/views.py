from django.contrib.auth import views as auth_views
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.http.response import HttpResponseRedirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from . import models, forms
from .forms import UserRegistrationForm
from django.shortcuts import render



class CheckProfileMixin(LoginRequiredMixin):
    redirect_on_missing_profile = True
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        user = self.request.user
        profile = models.CustomerProfile.objects.filter(user__pk=user.pk)
        redirect_needed = bool(profile)
        if self.redirect_on_missing_profile is True:
            redirect_needed = not redirect_needed
        if redirect_needed:
            return HttpResponseRedirect(self.profile_redirect_url)

        return super().dispatch(request, *args, **kwargs)


class CustomerProfileCreate(CheckProfileMixin, generic.CreateView):
    profile_redirect_url = reverse_lazy("accounts:profile")
    redirect_on_missing_profile = False
    model = models.CustomerProfile
    template_name = "acc/profile_form.html"
    fields = [
        "first_name",
        "last_name",
        "email",
        "code",
        "phone",
        "country",
        "city",
        "home_index",
        "address1",
        "address2",
    ]
    form = forms.CustomerProfileForm

    def get_form(self, **kwargs):
        form = super().get_form(**kwargs)
        if self.request.user.is_authenticated:
            form.fields['first_name'].initial = self.request.user.first_name
            form.fields['last_name'].initial = self.request.user.last_name
            form.fields['email'].initial = self.request.user.email
        return form
    
    def form_valid(self, form):
        success_url = reverse_lazy("accounts:profile")
        profile = form.save(commit=False)
        profile.user = self.request.user
        profile.save()
        self.object = profile
        return HttpResponseRedirect(success_url)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["headline"] = 'Создание профиля'
        return context



class CustomerProfileDetail(CheckProfileMixin, generic.DetailView):
    profile_redirect_url = reverse_lazy("accounts:profile-create")
    redirect_on_missing_profile = True
    template_name = "acc/profile.html"

    def get_object(self):
        user = self.request.user
        profile = models.CustomerProfile.objects.filter(user__pk=user.pk)
        if profile:
            profile = profile[0]
        else:
            profile = models.CustomerProfile.objects.create(
                username=user,
                first_name = self.first_name,
                last_name = self.last_name,
                email = "fill in",
                code = "chose",
                phone = "fill in",
                country = "fill in",
                city = "fill in",
                home_index = "fill in",
                address1 = "fill in",
                address2 = "fill in"
            )
        return profile


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'acc/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'acc/register.html', {'user_form': user_form})

class CustomerProfileUpdate(CheckProfileMixin, generic.UpdateView):
    model = models.CustomerProfile
    template_name = "acc/profile_form.html"
    fields = [
        "first_name",
        "last_name",
        "email",
        "code",
        "phone",
        "country",
        "city",
        "home_index",
        "address1",
        "address2",
    ]

    def get_object(self):
        user = self.request.user
        profile = models.CustomerProfile.objects.filter(user__pk=user.pk)
        if profile:
            profile = profile[0]
        return profile
    
    def form_valid(self, form):
        success_url = reverse_lazy("accounts:profile")
        profile = form.save(commit=False)
        profile.user = self.request.user
        profile.save()
        self.object = profile
        return HttpResponseRedirect(success_url)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["headline"] = 'Редактирование профиля'
        return context
