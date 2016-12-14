from django.db import models


class Information(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    jabber = models.CharField(max_length=30)
    skype = models.CharField(max_length=30)
    other_contacts = models.TextField()
    bio = models.TextField()
    birth_date = models.DateField()

    def __str__(self):
        return ' '.join([self.first_name, self.last_name])

