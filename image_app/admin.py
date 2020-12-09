from django.contrib import admin
# from __future__ import unicode_literals
from .models import Post, Tag

admin.site.register(Post)
admin.site.register(Tag)
