from django.db import models

class Blog(models.Model):
    image = models.ImageField(upload_to="image/")
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
