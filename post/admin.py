from django.contrib import admin
from .models import SharePost, SaveCollection, likeusers
# Register your models here.

admin.site.register(SharePost)
admin.site.register(SaveCollection)
admin.site.register(likeusers)