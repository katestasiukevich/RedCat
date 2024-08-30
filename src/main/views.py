from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from . import forms

# Create your views here.
def index(request):
    context = {
        'title': 'RED CAT - Главная',
    }
    return render(request, template_name="main/index.html", context=context)

def about(request):
    context = {
        'title': 'RED CAT - О нас',
    }
    return render(request, template_name="main/about.html", context=context)

def delivery_and_paiment(request):
    context = {
        'title': 'RED CAT - Доставка и оплата',
    }
    return render(request, template_name="main/delivery_and_paiment.html", context=context)


def contacts(request):
    context = {
        'title': 'RED CAT - Контактная информация',
    }
    return render(request, template_name="main/contacts.html", context=context)

def contact_form(request):
    if request.method == "GET":
        form = forms.ContactForm()
        context = {"form": form}
        return render(request, template_name="main/contact_form.html", context=context)
    if request.method == "POST":
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            pass  # send_email_to_admin(data)
        else:
            context = {"form": form}
            return render(
                request, template_name="main/contact_form.html", context=context
            )
        return HttpResponseRedirect(reverse_lazy("main:message-sent"))


def message_sent(request):
    return render(request, template_name="main/message-sent.html")