from django.db import models

class Languages(models.Model):
    language_name = models.CharField(max_length=80)
    country_image = models.ImageField(upload_to='dynamicimage',default="")

class Review(models.Model):
    rewiew = models.CharField(max_length=200)