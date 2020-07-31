from django.contrib import admin
from polls.models import Question, Choice
# Register your models here.
admin.site.register(Question)  # 괄호안에는 클래스 이름이 들어가야함
admin.site.register(Choice)

