from django.db import models

class Blog(models.Model):
    image = models.ImageField(upload_to="image/")
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    def __str__(self):
        return self.title


    def summary(self):
        return self.body[:100]
    def pub_date_short(self):
        return self.pub_date.strftime('%b %e %Y')
