from django.db import models

class Post(models.Model):
    nomi = models.CharField(max_length=50)
    mazmuni = models.TextField()
    soni = models.IntegerField(default=1)
    daromadi = models.IntegerField(default=1)

    # class Meta:
    #     verbose_name = "Post"
    #     verbose_name_plural = "Postlar"

    def __str__(self):
        return f'{self.nomi}'

