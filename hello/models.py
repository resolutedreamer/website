from django.db import models
from django.conf import settings

class Customer(models.Model):
    username = models.CharField(max_length=30, primary_key=True)
    password = models.CharField(max_length=30, blank=False)
    email = models.CharField(max_length=30, blank=False)
    phone = models.CharField(max_length=10, blank=False)
    token = models.CharField(max_length=50, blank=True)

    class Meta: 
        verbose_name_plural = 'customers'

    def __unicode__(self):
        return u"%s's Customer Info" % self.username
