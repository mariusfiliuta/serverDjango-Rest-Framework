from __future__ import unicode_literals

from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length = 255)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"
        db_table = "category"


class Play(models.Model):
    name            = models.CharField(max_length=255)
    description     = models.CharField(max_length=500)
    #image_paths    = ArrayField(models.CharField(max_length = 255), null=True, blank=True)
    image_paths     = models.CharField(max_length=255)
    trailer_link    = models.CharField(max_length=255, default='')
    category        = models.ForeignKey(Category, related_name='plays', on_delete = models.CASCADE)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "play"


class Theater(models.Model):

    '''
    CITIES = (
        'Bucharest',
        'Alba',
        'Iulia',
        'Arad',
        'Baia',
        'Mare',
        'Brasov',
    'Brail',
        'Cluj - Napoca',
        'Constanta',
        'Craiova',
        'Deva',
        'Galati',
        'Iasi',
        'Oradea',
        'Satu',
        'Mare',
        'Sibiu',
        'Sighisoara',
        'Suceava',
        'Timisoara',
        'Targu',
        'Jiu',
        'Targu',
        'Mures',
        'Tulcea',
        '',
    )
    CITIES_CHOICES = ((i, i) for i in CITIES)
    '''

    name        = models.CharField(max_length = 255)
    latitude    = models.DecimalField(max_digits = 9, decimal_places = 6)
    longitude   = models.DecimalField(max_digits = 9, decimal_places = 6)
    #city        = models.CharField(max_length=255, choices=CITIES_CHOICES, default='')
    city        = models.CharField(max_length=255, default='')

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "theater"


class Actor(models.Model):
    first_name      = models.CharField(max_length = 255)
    last_name       = models.CharField(max_length = 255)
    profile_picture = models.CharField(max_length = 255)
    description     = models.CharField(max_length = 500)

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        db_table = "actor"


class Play_Representation(models.Model):

    theater     = models.ForeignKey(Theater, related_name='play_representations', on_delete = models.CASCADE)
    play        = models.ForeignKey(Play, related_name='play_representations', on_delete = models.CASCADE)
    date        = models.DateTimeField()
    actors      = models.ManyToManyField(Actor, related_name='play_representations')

    def __unicode__(self):
        return 'Representation of the play ' + self.play.name + ' at the theater ' + self.theater.name

    class Meta:
        db_table = "play_representation"

'''
class User(models.Model):
    first_name      = models.CharField(max_length = 255)
    last_name       = models.CharField(max_length = 255)
    profile_picture = models.CharField(max_length = 255)
    username        = models.CharField(max_length = 255)
    email           = models.EmailField(max_length = 255)

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name


    class Meta:
        db_table = "user"

'''


class Profile(models.Model):
    profile_picture = models.CharField(max_length=255)
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE, primary_key=True)
    def __unicode__(self):
        return self.user.username

class Comment(models.Model):
    user            = models.ForeignKey(User, related_name='comments', on_delete = models.CASCADE)
    play            = models.ForeignKey(Play, related_name='comments', on_delete = models.CASCADE)
    comment_text    = models.CharField(max_length=500)
    created         = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return 'Comment by ' + self.user.get_full_name() + ' for play ' + self.play.name

    class Meta:
        db_table = "comment"


class Rating(models.Model):
    user            = models.ForeignKey(User, related_name='ratings', on_delete = models.CASCADE)
    play            = models.ForeignKey(Play, related_name='ratings', on_delete = models.CASCADE)
    rating_number   = models.IntegerField(default = 0)

    def __unicode__(self):
        return 'Rating by ' + self.user.__unicode__() + ' for play ' + self.play.name

    class Meta:
        db_table = "rating"


class Favorite(models.Model):
    user = models.ForeignKey(User, related_name='favorites', on_delete=models.CASCADE)
    play = models.ForeignKey(Play, related_name='favorites', on_delete=models.CASCADE)
    is_favorite = models.BooleanField(default=False)

    def __unicode__(self):
        return 'Favorite status for play ' + self.play.name + ' on user ' + self.user.__unicode__() + ' is ' + self.is_favorite.__str__()

    class Meta:
        db_table = "favorite"


class WebUsers(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    class Meta:
        db_table = "webusers"
