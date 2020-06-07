from django.contrib import admin
from django.urls import path
from contacts.views import listView, createContactView, update_contact,delete_contact


urlpatterns = [
    path('', listView, name='home'),
    path('create', createContactView, name='create'),
    path('update/<int:id>',update_contact,name='update' ),
    path('delete/<int:id>', delete_contact, name='delete')


]