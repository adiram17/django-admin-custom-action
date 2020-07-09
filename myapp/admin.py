from django.contrib import admin
from .models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'author', 'year', 'description')

    actions = ['setOutOfStock', ]

    def setOutOfStock(self, request, queryset):
        queryset.update(status='outstock')
    setOutOfStock.short_description = "Set selected as Out of Stock"

admin.site.register(Book, BookAdmin)


