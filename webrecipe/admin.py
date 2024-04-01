from django.contrib import admin
from .models import *
# Register your models here.
admin.site.site_title="Share Food Recipe"
admin.site.site_header='Simple Recipe'
admin.site.index_title='Recipe'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('name',)
    search_fields=('name',)

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    fields=(('name','category'),'description','ingredient','instruction','image')
    list_display=('name','description','category','created')
    ordering=('name',)
    search_fields = ('name','category__name')
    list_filter= ('category',)
    # autocomplete_fields=('')
    list_per_page=10