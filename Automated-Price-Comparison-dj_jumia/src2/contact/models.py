from django.db import models

# Create your models here.

class Contact(models.Model):
    name         =  models.CharField(max_length=200 , blank=True, null=True)
    email        =  models.EmailField()
    phone_number =  models.CharField(max_length=16 , blank=True, null=True)
    message      = models.TextField()


    def __str__(self):
        return self.name