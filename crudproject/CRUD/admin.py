from django.contrib import admin
from .models import booklist

# Register your models here.
class booklistAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'author')
    
    
    
admin.site.register(booklist,booklistAdmin)