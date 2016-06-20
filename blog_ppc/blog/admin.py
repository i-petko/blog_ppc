from django.contrib import admin
from django.db import models

from .models import BlogPost, Author

admin.site.register(BlogPost)
admin.site.register(Author)