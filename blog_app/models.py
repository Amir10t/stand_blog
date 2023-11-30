from django.db import models
from PIL import Image
from django.shortcuts import reverse

# Create your models here.

class PostCategoryModel(models.Model):
    title = models.CharField(max_length=300, db_index=True, verbose_name='title')
    url_title = models.CharField(max_length=300, db_index=True, verbose_name='name in url')
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'( {self.title} - {self.url_title} )'

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class PostModel(models.Model):
    title = models.CharField(max_length=80, verbose_name="title")
    image = models.ImageField(upload_to='images/posts', null=True, blank=True, verbose_name='image post (770*340px)')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="created date")
    short_description = models.CharField(max_length=200, verbose_name="short description")
    description = models.TextField(blank=True ,verbose_name="description")
    category = models.ManyToManyField(
        PostCategoryModel,
        related_name='post_categories',
        verbose_name='categories')
    slug = models.SlugField(default="", null=False, max_length=200, unique=True,
                            verbose_name='name in url')
    active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('detail-page', args=[self.slug])

    def __str__(self):
        return self.slug

    class Meta():
        verbose_name = "post"
        verbose_name_plural = "posts"


class CommentPostModel(models.Model):
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='post_comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']
        verbose_name = "comment"
        verbose_name_plural = "comments"

    def __str__(self):
        return 'Comment {} by {}'.format(self.message, self.name)
