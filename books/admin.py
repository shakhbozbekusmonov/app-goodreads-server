from django.contrib import admin
from books.models import Book


class BookAdmin(admin.ModelAdmin):
    search_fields = ('title', 'isbn')


admin.site.register(Book, BookAdmin)
admin.site.site_header = "Goodreads"
