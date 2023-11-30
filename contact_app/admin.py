from django.contrib import admin
from .models import ContactModel

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_filter = ['is_read_by_admin']
    list_display = ['name','is_read_by_admin']
    list_editable = ['is_read_by_admin']

admin.site.register(ContactModel, ContactAdmin)