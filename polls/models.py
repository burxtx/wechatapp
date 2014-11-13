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
    votes = models.IntegerField(default=0, null=True, blank=True)
    optional_text = models.CharField(max_length=300, null=True, blank=True)
    score = models.IntegerField(null=True, blank=True)
    def __unicode__(self):
        return self.choice_desc

class PollUser(models.Model):
    """docstring for PollUser"""
    MALE = 1
    FEMALE = 0
    GENDER_CHOICE = (
        (MALE, '男'),
        (FEMALE, '女'),
        )
    LT35 = 1
    ST35 = 0
    AGE_CHOICE = (
        (LT35, '大于35'),
        (ST35, '小于35'),
        )
    # username = models.CharField()
    age = models.IntegerField(choices=AGE_CHOICE, null=True, blank=True, verbose_name="年龄")
    gender = models.IntegerField(choices=GENDER_CHOICE, null=True, blank=True, verbose_name="性别")

    # subscribe = models.IntegerField()
    openid = models.CharField(max_length=500, null=True, blank=True)
    nickname = models.CharField(max_length=200, null=True, blank=True, verbose_name="名字")
    sex = models.IntegerField(null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    province = models.CharField(max_length=100, null=True, blank=True)
    # language = models.CharField(max_length=100, null=True, blank=True)
    headimgurl = models.CharField(max_length=500, null=True, blank=True)
    privilege = models.CharField(max_length=200, null=True, blank=True)
    # subscribe_time = models.DateTimeField(null=True, blank=True)
    def __unicode__(self):
        # return '%s, %s' % (self.age, self.gender)
        return self.nickname

class Answer(models.Model):
    """docstring for Answer"""
    pid = models.ForeignKey(Poll, null=True, blank=True)
    qid = models.ForeignKey(Question, null=True, blank=True)
    cid = models.ForeignKey(Choice, null=True, blank=True)
    uid = models.ForeignKey(PollUser, null=True, blank=True)
    submit_time = models.DateTimeField(auto_now_add=True)
    #add answer date and time
    def __unicode__(self):
        return self.cid and self.cid.choice_desc or ''

    def get_u_age(self):
        return self.uid and self.uid.get_age_display() or ''
    get_u_age.short_description = '年龄'

    def get_u_gender(self):
        return self.uid and self.uid.get_gender_display() or ''
    get_u_gender.short_description = '性别'

    def get_q_question_desc(self):
        return self.qid and self.qid.question_desc or ''
    get_q_question_desc.short_description = '问题'

    def get_c_choice_desc(self):
        return self.cid and self.cid.choice_desc or ''
    get_c_choice_desc.short_description = '选择'