// $("body").data("url", {{ url }});
var APPID = "wxff35be27e6a08ec6";
var REDIRECT_URI = encodeURIComponent("http://co.jiutianwai.com/wechatapp/polls/home?pid=1");
var SCOPE = "snsapi_userinfo";
var url = "https://open.weixin.qq.com/connect/oauth2/authorize?appid="+APPID+"&redirect_uri="+REDIRECT_URI+"&response_type=code&scope="+SCOPE+"&state=STATE#wechat_redirect"
var imgUrl = "http://co.jiutianwai.com/wechatapp/static/polls/img/aaa.jpg";
var lineLink = url;
var descContent = '';
var shareTitle = '测测你的睡仙指数';
var appid = '';