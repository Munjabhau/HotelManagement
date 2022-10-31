from django.contrib import admin
from food.models import *


# Register your models here.
class ChineseAdmin(admin.ModelAdmin):
    list_display = ('name', 'priceH', 'priceF')


admin.site.register(Chinese, ChineseAdmin)
admin.site.register(Order)
admin.site.register(Item)
