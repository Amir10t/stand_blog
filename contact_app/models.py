from django.db import models

# Create your models here.

class ContactModel(models.Model):
    name = models.CharField(max_length=50, verbose_name="name")
    email = models.EmailField(max_length=150, verbose_name="email")
    subject = models.CharField(max_length=150, verbose_name="subject")
    message = models.TextField(verbose_name="message")
    is_read_by_admin = models.BooleanField(verbose_name='Is Read By Admin', default=False)

    def __str__(self):
        return f"{self.name} -> {self.subject}"

    class Meta():
        verbose_name = "message"
        verbose_name_plural = "messages"