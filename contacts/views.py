from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.views import View
from django.views import generic
from contacts.models import contact, number
from django.template import loader
from django.urls import reverse

class index(View):
    def get(self,request):
        contacts_list = contact.objects.order_by("name")[:5]
        template = loader.get_template("contacts/index.html")
        context = {
            "contacts_list": contacts_list,
        }
        return HttpResponse(template.render(context, request))
class detail(View):
    def get(self,request, contact_id):
        contact_selected = contact.objects.get(id=contact_id)
        template = loader.get_template("contacts/details.html")
        numbers = [i.number for i in contact_selected.number.all()]
        context = {
            "contact": contact_selected, 'numbers': numbers
        }
        return HttpResponse(template.render(context, request))
    
class add(View):
    def get(self, request):
        template = loader.get_template("contacts/form.html")
       
        return HttpResponse(template.render({}, request))

def post_contact(request):
        a = contact.objects.create(name=request.POST['name'], work=request.POST['work'])
        b = number.objects.create(number=request.POST['number'], oc_key=a)

        
        return HttpResponseRedirect(reverse("contacts:index"))



# Create your views here.
