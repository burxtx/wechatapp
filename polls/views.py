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

def home_page(request, openid):
    if request.method=="POST":
        u, created = PollUser.objects.get_or_create(openid="")
        gender = request.POST['gender']
        age = request.POST['age']
        # if not created:
        u.gender = gender
        u.age = age
        u.save()
        json = simplejson.dumps({'success': True})
        return HttpResponse(json, mimetype='application/json')
    if request.method=="GET":
        u, created = PollUser.objects.get_or_create(openid="")
        return render_to_response('polls/home.html')
        
def answer_question(request):
    if request.method=="GET":
        qid = request.GET.get("qid")
        q = Question.objects.get(pk=qid)
        p = Poll.objects.get(pk=q.poll.id)
        qnum = Question.objects.filter(poll=q.poll.id)

        c = Choice.objects.filter(question=q)
        variables={
            "p": p,
            "q": q,
            "c": c,
        }
        if q.qindex <= qnum:
            return render_to_response("polls/question.html", variables)
        else:
            return HttpResponseRedirect("/polls/result")
    if request.method=="POST":
        print request.POST
        # vote = request.POST["vote"]
        qid = request.POST["qid"]
        uid = request.POST["uid"]
        cid = request.POST["cid"]
        a, created = Answer.objects.get_or_create(uid=uid, cid=cid, qid=qid)
        a.qid = qid
        a.uid = uid
        a.cid = cid
        a.save()
        json = simplejson.dumps({'success': True})
        return HttpResponse(json, mimetype="application/json")
        # return HttpResponseRedirect("/polls/question/%d" % qid)

def get_result(request):
    if request.method=="GET":
        total = 0
        pid = request.GET.get("pid")
        a = Answer.objects.filter(uid=uid, pid=pid, )
        for answer in a:
            total += a.cid.score
        variables = {
            "total": total,
        }
        return render_to_response("polls/result.html", variables)

