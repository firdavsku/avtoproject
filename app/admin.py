from django.contrib import admin

# Register your models here.
from .models import Car, Category

admin.site.register(Category)


class CarAdmin(admin.ModelAdmin):
    list_display = ['id','name','type']
    search_fields = ['name']
admin.site.register(Car, CarAdmin)