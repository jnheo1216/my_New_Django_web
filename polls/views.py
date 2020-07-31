from django.shortcuts import render, get_object_or_404
from polls.models import Question
# Create your views here.

# 클라이언트가 서버에 요청울 보내는 작업 => request
# 클라이언트가 서버에 요청울 보낼때 여러가지 정보가 같이 제공
# 이 내용을 request라는 객체로 만들어 사용
# 서버가 클라이언트에 요청을 보내는 작업 => response

# Question class의 객체 3개를 리스트 안으로


def index(request):
    # 모든 객체 다 가져와야해
    tmp = Question.objects.all().order_by('-pub_date')[:3]
    context = {"latest_question_list": tmp}

    return render(request, 'index.html', context)


def detail(request, question_id):
    # 특정 객체 하나만 가져와야해
    tmp = get_object_or_404(Question, pk=question_id)
    context = {"question": tmp}
    return render(request, 'detail.html', context)