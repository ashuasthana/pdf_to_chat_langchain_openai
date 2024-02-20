from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='pdf_doc', blank=True)
    vector = models.TextField(blank=True)  # Store vector representation here

    def __str__(self):
        return self.title
