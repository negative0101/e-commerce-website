from django.db import models


# Create your models here.

class Contact(models.Model):
    MAX_LEN_SUBJECT = 255
    email = models.EmailField()
    subject = models.CharField(max_length=MAX_LEN_SUBJECT)
    message = models.TextField()

    def __str__(self):
        return self.email
