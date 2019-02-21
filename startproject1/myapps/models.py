from django.db import models
import datetime

# Create your models here.

from django.db import models
from django.utils import timezone


# this is my app page on were you you use the page


class myapps(models.Model):
    book_name = models.CharField(max_length=100)
    book_pagenumber = models.IntegerField()
    book_genre = models.DateField()


class Question(models.Model):
    question_text = models.CharField(max_length=100)
    date_pub = models.DateTimeField('date publish')