from django.contrib import admin
from .models import *


# Register your models here.
class categAdmin (admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}


admin.site.register(categ, categAdmin)


class prodAdmin (admin.ModelAdmin):
    list_display = ['name','slug','price','stock','img']
    list_editable = ['price','stock','img']
    prepopulated_fields = {'slug': ['name']}


admin.site.register(product, prodAdmin)
