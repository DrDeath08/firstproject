from django.db import models

# Create your models here.
class Anime(models.Model):
    title = models.CharField(max_length = 255)
    studio = models.CharField(max_length = 255)
    year = models.IntegerField()
    comments = models.CharField(max_length=1000, default='')

    def __str__(self):
        return self.title
