from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path('about/', views.about, name="about"),
    path('delivery&paiment/', views.delivery_and_paiment, name="delivery-and-paiment"),
    path('contacts/', views.contacts, name="contacts"),
    path('contact-us/', views.contact_form, name="contact-us"),
    path('message-sent/', views.message_sent, name="message-sent"),
]