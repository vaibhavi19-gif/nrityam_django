from django.db import models


class Cinfo(models.Model):
    Fullname = models.CharField(max_length=150)
    Email = models.TextField()
    Username = models.TextField()
    Password = models.TextField()

    def __str__(self):
        return "{0}".format(self.Fullname)

