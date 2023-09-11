from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils import timezone 
from django.urls import reverse
from uuid import uuid4
from django_resized import ResizedImageField

import os

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    addressLine1= models.CharField(null=True, blank=True, max_length=200)
    addressLine2=models.CharField(null=True, blank=True, max_length=200)
    city=models.CharField(null=True, blank=True, max_length=200)
    province=models.CharField(null=True, blank=True, max_length=200)
    country=models.CharField(null=True, blank=True, max_length=200)
    postalCode=models.CharField(null=True, blank=True, max_length=200)
    profileImage=ResizedImageField(size=[200, 200], quality=75, upload_to='profile')



    #utility variable

    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug= models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created=models.DateTimeField(blank=True, null=True)
    last_updated= models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return '{} {} {}'.format(self.user.first_name, self.user.last_name, self.user.email)
    
    def get_absolute_url(self):
        return reverse('contact-detail', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueid is None:
            self.uniqueid = str(uuid4()).split('-')[4]
            self.slug = slugify('{}{}'.format(self.title, self.uniqueid))


        self.slug = slugify('{}{}'.format(self.title, self.uniqueid))
        self.last_updated = timezone.localtime(timezone.now())
        super(contact, self).save(*args, **kwargs)