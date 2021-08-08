from django.contrib import admin
from .models import Post
# To make our model visible on the admin page, 
# we need to register the model with admin.site.register(Post)
admin.site.register(Post)
