from django.contrib import admin
from .models import Document
# Register your models here.
@admin.register(Document)
class DocumneAdmin(admin.ModelAdmin):
    list_display=['id','vector','file','vector']