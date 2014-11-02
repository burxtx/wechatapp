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
import urllib2, json
from urllib import quote

pdb.set_trace()

def gen_scope_url():
    APPID = "wx455601ff052bea31" #随手换测试号
    REDIRECT_URI = quote("yikf.jiutianwai.com/wechatapp/polls/home?pid=1") #调查系统url
    SCOPE = "snsapi_userinfo"
    url = "https://open.weixin.qq.com/connect/oauth2/authorize?appid=%s&redirect_uri=%s&response_type=code&scope=%s&state=STATE#wechat_redirect"\
    % (APPID, REDIRECT_URI, SCOPE)
    return url
def gen_access_token_url(code):
    APPID = "wx455601ff052bea31"
    SECRET = "647bb7f32155cb2b794337145debf105"
    CODE = code
    url = "https://api.weixin.qq.com/sns/oauth2/access_token?appid=%s&secret=%s&code=%s&grant_type=authorization_code"\
    % (APPID, SECRET, CODE)
    return url
def gen_user_info_url(access_token, openid):
    url = "https://api.weixin.qq.com/sns/userinfo?access_token=%s&openid=%s&lang=zh_CN" % (access_token, openid)
    return url
def get_json_response(url):
    response = urllib2.urlopen(url).read()
    dict_data = json.loads(response)
    return dict_data

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
        url = gen_scope_url()
        print url
        if "code" in request.GET:
            code = request.GET.get("code", "")
            access_token_url = gen_access_token_url(code)
            dict_data = get_json_response(access_token_url)
            access_token = dict_data["access_token"]
            openid = dict_data["openid"]
            user_info = get_json_response(access_token, openid)
            request.session["openid"] = openid
            print openid
            u, created = PollUser.objects.get_or_create(openid=openid)

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

