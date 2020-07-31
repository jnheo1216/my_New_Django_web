from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    # table의 id column은 default로 지정이 되요
    # id가 primary key, Not Null, Unique
    # id는 autoincrement 특성을 가지는 정수형으로 지정
    # 자동으로 생성해주기 때문에 class정의에서 나오지 않아요!!
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question,
                                    on_delete=models.CASCADE)  # 지울떄 같이지워버린다는뜻
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text