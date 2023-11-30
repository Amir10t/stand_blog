from django.db import models

# Create your models here.

class FooterLink(models.Model):
    title = models.CharField(max_length=50)
    url = models.URLField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "link"
        verbose_name_plural = "links"