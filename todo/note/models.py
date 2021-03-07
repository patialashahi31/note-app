from django.db import models

# Create your models here.

class Note(models.Model):
    title = models.CharField(null=True,blank=True,max_length=200)
    description = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.title
    