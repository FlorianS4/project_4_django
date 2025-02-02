from django.db import models

# Create your models here.


class GameCritContact(models.Model):
    """
    Model to contact the side owner. and talk about
    the blog or bring forth ideas to implement
    """

    contact_email = models.EmailField(max_length=200)
    contact_field = models.TextField()
    contact_created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.contact_field} | submitted by {self.contact_email}"
