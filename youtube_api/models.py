from django.db import models

# Create your models here.

class Cricket(models.Model):

    videoId = models.CharField(max_length=50,unique=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    # publishedAt = models.CharField(max_length=100)
    publishedAt = models.DateTimeField()
    thumbUrl = models.CharField(max_length=100)

    class Meta:
        indexes = [
            models.Index(fields=['-publishedAt']),
        ]

    def __str__(self):
        return str(self.id)
