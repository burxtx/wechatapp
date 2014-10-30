#coding: UTF-8
from django.db import models

# Create your models here.

class Poll(models.Model):
    """docstring for Poll"""
    poll_name = models.CharField(max_length=100)
    poll_desc = models.CharField(max_length=200,null=True,blank=True)
    ptype = models.IntegerField(null=True,blank=True,verbose_name="poll type")
    def __unicode__(self):
        return self.poll_name

class Question(models.Model):
    """docstring for Question"""
    question_desc = models.CharField(max_length=200)
    qindex = models.IntegerField(null=True,blank=True,verbose_name="index")
    qtype = models.CharField(max_length=100, null=True, blank=True, verbose_name="question type")
    poll = models.ForeignKey(Poll)

    def __unicode__(self):
        return self.question_desc

class Choice(models.Model):
    """docstring for Choice"""
    A = 1
    B = 2
    C = 3
    D = 4
    E = 5
    F = 6
    G = 7
    H = 8
    I = 9
    J = 10
    OPTION_CHOICE = (
        (A, "A"),(B, "B"),(C, "C"),(D, "D"),(E, "E"),(F, "F"),
        (G, "G"),(H, "H"),(I, "I"),(J, "J"),)
    question = models.ForeignKey(Question)
    choice_desc = models.CharField(max_length=100)
    cindex = models.IntegerField(choices=OPTION_CHOICE, null=True, blank=True, verbose_name="index")
    votes = models.IntegerField(null=True, blank=True)
    optional_text = models.CharField(max_length=300, null=True, blank=True)
    score = models.IntegerField(null=True, blank=True)
    def __unicode__(self):
        return self.choice_desc

class PollUser(models.Model):
    """docstring for PollUser"""
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
    poll = models.ManyToManyField(Poll)
    question = models.ManyToManyField(Question)
    choice = models.ManyToManyField(Choice)
    # username = models.CharField()
    age = models.IntegerField(choices=AGE_CHOICE, null=True, blank=True)
    gender = models.IntegerField(choices=GENDER_CHOICE, null=True, blank=True)

    subscribe = models.IntegerField()
    openid = models.CharField(max_length=500, null=True, blank=True)
    nickname = models.CharField(max_length=200, null=True, blank=True)
    sex = models.IntegerField(null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    province = models.CharField(max_length=100, null=True, blank=True)
    language = models.CharField(max_length=100, null=True, blank=True)
    headimgurl = models.CharField(max_length=500, null=True, blank=True)
    subscribe_time = models.DateTimeField(null=True, blank=True)
    def __unicode__(self):
        return '%s, %s' % (self.age, self.gender)