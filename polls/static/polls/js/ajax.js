function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');

$(".vote").click(function(){
    var choiceId = $(this).attr("id");
    var qId = $(".question").attr("id");
    var qIndex = $(".question_index");
    var data = {
        "qid": qId,
        "cid": choiceId,
        "csrfmiddlewaretoken": csrftoken
    };
    var url = "{% url 'polls:question' %}?pid=1&qindex="+qIndex;
    $.post(url, data,
        function(){
        window.location.assign("{% url 'polls:question' %}?pid=1&qindex="+(qIndex+1))
    });
});