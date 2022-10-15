from django.db import models
from django.contrib.auth.models import User

from django.core.exceptions import ValidationError

# sending signal
from django.dispatch import receiver
from django.db.models.signals import post_save

BAD_WORDS = ['java', 'C#', 'nodejs', 'C++', 'php']


def no_bad_words_validator(name):
    """ -- Identifies Bad words and raises a Validation Error"""
    if any(word in name.lower() for word in BAD_WORDS):
        raise ValidationError('This text contains bad words!')


class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=150, validators=[no_bad_words_validator])
    address = models.CharField(max_length=300)
    zip_code = models.CharField('Zip Code', max_length=20, blank=True)
    phone = models.CharField('Contact phone', max_length=20, blank=True)
    web = models.URLField('website Address', blank=True)
    email = models.EmailField('Email', blank=True)
    owner = models.IntegerField('venue owner', blank=False, default=1)

    def __str__(self):
        return self.name


class ClubUser(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField('Email')


    def __str__(self):
        return str(self.first_name) + ' ' + str(self.last_name)


class Event(models.Model):
    name = models.CharField('event name', max_length=120, validators=[no_bad_words_validator])
    event_date = models.DateTimeField('event Date')
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    # venue = models.CharField('venue', max_length=120)
    manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    description = models.TextField(blank=True, validators=[no_bad_words_validator])
    attendees = models.ManyToManyField(ClubUser, blank=True)

    def __str__(self):
        return self.name



