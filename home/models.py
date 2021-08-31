from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=20)
    desc = models.TextField()
    pub_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.title