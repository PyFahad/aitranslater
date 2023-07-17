from django.contrib import admin
from .models import Languages,Review
# Register your models here.

class Display(admin.ModelAdmin):
    list_display = ['id','language_name','country_image']

class Rewiedesplay(admin.ModelAdmin):
    list_display=['rewiew']
admin.site.register(Languages,Display)
admin.site.register(Review,Rewiedesplay)