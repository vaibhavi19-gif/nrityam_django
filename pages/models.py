from django.db import models


class Feedback(models.Model):
    Username = models.TextField(max_length=100)
    Email = models.EmailField()
    Course = models.CharField(max_length=100)
    Rate = models.CharField(max_length=100)
    Need = models.TextField()


def __str__(self):
    return self.title