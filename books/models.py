from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Books(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    year = models.IntegerField(blank=False)
    country = models.CharField(max_length=200)
    genre = models.ForeignKey("Genre", on_delete=models.PROTECT, null=False)
    price = models.TextField(blank=False)


    def __str__(self):
        return self.author


class Genre(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name 
    

class Rating(models.Model):
    book = models.ForeignKey(Books, related_name='rating', on_delete=models.CASCADE)
    one = models.PositiveIntegerField(default=0, null=True, blank=False)
    two = models.PositiveIntegerField(default=0, null=True,blank=False)
    three = models.PositiveIntegerField(default=0, null=True, blank=False)
    four = models.PositiveIntegerField(default=0, null=True,blank=False)
    five = models.PositiveIntegerField(default=0, null=True,blank=False)

    def __str__(self):
        book_rating = {
            '1': self.one,
            '2': self.two, 
            '3': self.three, 
            '4': self.four,
            '5': self.five,
        }
        max_rating = max(book_rating.values())
        return str(max_rating)
    

class WeeklyRecommendation(models.Model):
    book = models.ForeignKey(Books, related_name='recommendation', on_delete=models.CASCADE)
    announcement = models.TextField(max_length=255)

    def __str__(self):
        return self.announcement
    





