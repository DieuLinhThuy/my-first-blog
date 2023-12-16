from django.contrib import admin
from blog import models
from blog.models import Post

admin.site.register(Post)