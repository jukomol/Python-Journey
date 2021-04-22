from django.contrib import admin

from .models import Food


class FoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'food_name', 'is_published', 'price', 'list_date', 'catagory')
    list_display_links = ('id', 'food_name')
    list_editable = ('is_published',)
    search_fields = ('food_name', 'description', 'price')
    list_per_page = 25


admin.site.register(Food, FoodAdmin)