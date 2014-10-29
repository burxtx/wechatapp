#coding: UTF-8
from django.db import models

# Create your models here.
class Question(models.Model):
    """docstring for Question"""
    question_text = models.CharField(max_length=200)

    def __unicode__(self):
        return self.question_text

class Poll(models.Model):
    """docstring for Poll"""
    question = models.ManyToManyField(Question)
    poll_name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.poll_name

class Choice(models.Model):
    """docstring for Choice"""
    question = models.ForeignKey(Question)
    choice = models.CharField(max_length=100)
    votes = models.IntegerField(blank=True)
    score = models.IntegerField()
    def __unicode__(self):
        return self.poll_name

class User(object):
    """docstring for User"""
    MALE = 1
    FEMALE = 0
    GENDER_CHOICE = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        )
    LT35 = 1
    ST35 = 0
    AGE_CHOICE = (
        (LT35, 'Large'),
        (ST35, 'Small'),
        )
    username = models.CharField()
    age = models.IntegerField(choices=AGE_CHOICE)
    gender = models.IntegerField(choices=GENDER_CHOICE)
    def __unicode__(self):
        return '%s, %s, %s' % (self.username, self.age, self.gender)