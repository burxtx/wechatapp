from django.contrib import admin

# Register your models here.
from polls.models import *

class AnswerAdmin(admin.ModelAdmin):
    list_display = ['uid','get_u_gender', 'get_u_age', 'get_q_question_desc', 'get_c_choice_desc']
    list_filter = ['uid__age', 'uid__gender', 'qid']

    def __init__(self,*args,**kwargs):
        super(AnswerAdmin, self).__init__(*args, **kwargs)
        self.list_display_links = (None, )

admin.site.register(Poll)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(PollUser)
admin.site.register(Answer, AnswerAdmin)