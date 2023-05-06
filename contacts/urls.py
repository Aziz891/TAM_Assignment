from django.urls import path
from contacts.views import index, detail, add, post_contact
from . import views

app_name = "contacts"
urlpatterns = [
   path('index/', index.as_view(), name='index'),
   path('form/', add.as_view(), name='form'),
   path('post_contact/', post_contact, name='post_contact'),
   path("<int:contact_id>/", detail.as_view() ,name="detail"),
]