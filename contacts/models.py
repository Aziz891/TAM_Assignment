from django.db import models

# Create your models here.
class contact(models.Model):
    id= models.AutoField(primary_key=True)
    name = models.CharField(max_length=500, blank=True, null=True)
    work = models.CharField(max_length=500, blank=True, null=True)
    

class number(models.Model):
      id= models.AutoField(primary_key=True)
      number = models.CharField(max_length=500, blank=True, null=True)
      oc_key = models.ForeignKey('contact', models.DO_NOTHING, db_column='contact_key', blank=True, null=True, related_name='number')
   