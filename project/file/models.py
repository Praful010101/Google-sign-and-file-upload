from django.db import models


class Upload(models.Model):
    title = models.CharField(max_length=50)
    upload = models.FileField(upload_to="media")
# Create your models here.
