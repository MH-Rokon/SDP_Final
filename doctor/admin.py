from django.contrib import admin

from . import models
from django.contrib import admin
from .models import Doctor,Profile,Category

admin.site.register(Profile)
admin.site.register(Category)

admin.site.register(models.AvailableTime)

class SpecializationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }
class DesignationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }
    
admin.site.register(models.Specialization, SpecializationAdmin)
admin.site.register(models.Designation, DesignationAdmin)
admin.site.register(models.Doctor)
admin.site.register(models.Review)