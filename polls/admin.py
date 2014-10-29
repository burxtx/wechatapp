from django.contrib import admin

# Register your models here.
from polls.models import Question, Choice, Poll

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Poll)