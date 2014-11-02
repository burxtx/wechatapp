# coding: utf-8
from django.shortcuts import render
import time, datetime
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.utils import simplejson
from django.core.urlresolvers import reverse
from polls.models import *
import pdb

pdb.set_trace()

def home_page(request):
    if request.method=="POST":
        if request.session.has_key("openid"):
            openid = request.session["openid"]
            u, created = PollUser.objects.get_or_create(openid=openid)
            gender = request.POST['gender']
            age = request.POST['age']
            # if not created:
            u.openid = openid
            u.gender = gender
            u.age = age
            u.save()
            # json = simplejson.dumps({'success': True})
            # return HttpResponse(json, mimetype='application/json')
        return HttpResponseRedirect("/wechatapp/polls/question?pid=1&qid=1")
    if request.method=="GET":
        openid = request.GET.get("openid")
        u, created = PollUser.objects.get_or_create(openid="openid")

        pid = request.GET.get("pid")
        # q = Question.objects.get(poll=pid, qindex=qindex)
        q = Question.objects.filter(poll=pid)
        num = Question.objects.filter(poll=pid).count()
        # p = Poll.objects.get(pk=pid)

        # c = Choice.objects.filter(question=q)
        variables=RequestContext(request, {
            # "p": p,
            "q": q,
            # "c": c,
            "num":len(q),
        })
        # RequestContext(request)
        # return render_to_response('polls/home.html',context_instance=RequestContext(request))
        return render_to_response('polls/home.html', variables)
def get_question(request):
    if request.method=="GET":
        pid = request.GET.get("pid")
        # qid = request.GET.get("qid")
        # q = Question.objects.get(poll=pid, qindex=qindex)
        q = Question.objects.filter(poll=pid)
        num = Question.objects.filter(poll=pid).count()
        # question = Question.objects.get(pk=qid)
        # choices = Choice.objects.filter(question=qid)
        # p = Poll.objects.get(pk=pid)
        qid_list = [question.id for question in q]
        # c = Choice.objects.filter(question=q)
        variables=RequestContext(request, {
            "q": qid_list,
            # "c": c,
            "num":len(q),
        })
        return render_to_response("polls/question_gen.html", variables)

def answer_question(request):
    if request.method=="POST":
        pid = request.POST["pid"]
        qid = request.POST["qid"]
        # uid = request.POST["uid"]
        cid = request.POST["cid"]

        a, created = Answer.objects.get_or_create(uid=uid, qid=qid)
        # a, created = Answer.objects.get_or_create(uid=uid, cid=cid, qid=qid)
        a.pid = pid
        a.qid = qid
        # a.uid = uid
        a.cid = cid
        a.save()
        json = simplejson.dumps({'success': True})
        return HttpResponse(json, mimetype="application/json")
        # return HttpResponseRedirect("/polls/question/%d" % qid)
    if request.method=="GET":
        qid = request.GET["qid"]
        q = Question.objects.get(pk=qid)
        choices = Choice.objects.filter(question=qid)
        variables = RequestContext(request, {
            "choices": choices,
            "q": q,
            })
        return render_to_response("polls/question.html", variables)
def get_result(request):
    '''获取poll下面uid每一个最近的选项作为计分项'''
    if request.method=="GET":
        total = 0
        pid = request.GET.get("pid")
        a = Answer.objects.filter(uid=uid, pid=pid).order_by('-submit_time')
        for answer in a:
            total += answer.cid.score
            answer.cid.votes += 1
        variables = RequestContext(request, {
            "total": total,
        })
        return render_to_response("polls/result.html", variables)

