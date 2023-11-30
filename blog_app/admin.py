from django.contrib import admin
from .models import PostModel, PostCategoryModel, CommentPostModel

# Register your models here.

admin.site.register(PostModel)
admin.site.register(PostCategoryModel)
admin.site.register(CommentPostModel)