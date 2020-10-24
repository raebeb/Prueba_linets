from django.contrib import admin
from .models import MasterProductsConfigurable
# Register your models here.
@admin.register(MasterProductsConfigurable) 
class MasterProductsConfigurableAdmin(admin.ModelAdmin):
    pass