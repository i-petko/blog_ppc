from django.contrib import admin

from .models import BlogPost, Author

admin.site.register(BlogPost)
admin.site.register(Author)
