
from django.urls import path
from . import views

app_name = "polls"  # 나중에 이름 겹치지 말라고


urlpatterns = [
    # https://localhost:8000/polls
    path('', views.index, name='index'),
    # https://localhost:8000/polls/<숫자 1~3>/
    path('<int:question_id>/', views.detail, name='datail')  # 꺾쇠 뜻 : 변하는 무언가가 들어감 그걸 추출해서 사용함
]
