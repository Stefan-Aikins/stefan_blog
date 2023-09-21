from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class About(models.Model):
    blogger = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    recent_interests = models.CharField(max_length=100)
    education = models.CharField(max_length=100)
    career = models.CharField(max_length=100)

    def __str__(self):
        return f"""
    Full Name : {self.blogger}
    Nationality : {self.nationality}
    Recent Interests : {self.recent_interests}
    Education : {self.education}
    Career : {self.career}
    """


class News(models.Model):
    reporter = models.CharField(max_length=100)
    date_published = models.DateTimeField(default=timezone.now)
    headline = models.CharField(max_length=200)
    content = models.CharField(max_length=2500)

    def __str__(self):
        return f"""
    Reporter : {self.reporter}
    Date Published : {self.date_published}
    Headline : {self.headline}
    Content : {self.content}
    """


class ContactMe(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    message = models.CharField(max_length=400)
    file = models.FileField()

    def __str__(self):
        return f"""
        First name : {self.firstname}
        Last name : {self.lastname}
        Message : {self.message}
    """
