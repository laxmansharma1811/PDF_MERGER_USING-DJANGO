from django.db import models

# Create your models here.

class PDFMerger(models.Model):
    file = models.FileField(upload_to='pdfs/')
    created_at = models.DateTimeField(auto_now_add=True)