
// <script type="text/javascript">
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

    function getNext(q, i){
        var choiceId = $("input[name='vote'][checked]").attr("id");
        var qId = $(".question").attr("id");
        // var qIndex = $(".question_index").attr("id");
        var data = {
            "qid": qId,
            "cid": choiceId,
            "csrfmiddlewaretoken": csrftoken
        };
        var url = "{% url 'polls:answer_question' %}?pid=1&qid="+q[i];
        if (i<=num-1){
            alert("before:"+i);
            $(".inner").load("{% url 'polls:answer_question' %}?pid=1&qid="+q[i+1]);
            i++;
            alert("after:"+i);
            }else{
                alert("iiiii");
                window.location.href("{% url 'polls:result' %}")
            }
        // $.post(url, data,
        //     function(){
        //         if (i<num){
        //             $(".question").load("{% url 'polls:answer_question' %}?pid=1&qid="+q[i+1]);
        //             i++;
        //         }else{
        //             window.location.replace("{% url 'polls:result' %}")
        //         }
        //     });
    }

    $(".clear").click(function(q, i){
        $(this).children('input').attr("checked",true);
        $(this).siblings().children('input').attr("checked",false);
        getNext(q, i);
    })
// </script>