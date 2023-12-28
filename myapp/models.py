from django.db import models
from django.db.models.functions import Now, Pi

# Create your models here.


class Image(models.Model):
    photo = models.ImageField(upload_to="myimage")
    date = models.DateTimeField(db_default=Now())
