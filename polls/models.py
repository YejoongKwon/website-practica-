from django.db import models
from django.utils import timezone
import datetime
#DB TABLE FOR 설문조사 주제
# Create your models here.
class Question(models.Model):#설문조사 주제 테이블
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date  published')#관리자 페이지에서 보여질 필드명

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        now = timezone.now()
        #self.pub_date는 설문조사 주제가 등록된 시점
        return now >= self.pub_date >= now - datetime.timedelta(days=1)
    #함수가 호출되는 시점보다 하루이전보다는 설문조사 주제가 나중에 등록되어야 True
    #날짜가 큰건 나중 일임.
    #즉 하루 이내면 True
    was_published_recently.boolean = True
    # 'WAS PUBLISHED RECENTLY' 열의 정렬 기준을 pub_date(설문조사 주제 생성 시간)로 세팅
    was_published_recently.admin_order_field = 'pub_date'
    # 'WAS PUBLISHED RECENTLY' 열의 이름 변경
    was_published_recently.short_description = 'Published recently?'

    #설문조사 주제가 등록된 시점은 이후여야함. 
    #함수가 호출되는 순간now 로부터 하루어치 차이값(현재 날짜 시간 기준)

#DB TABLE FOR 설문조사 주제별 선택지
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)#괄호 안에 아무것도 적지 않으면 Question 테이블의 primary key 인 id를 땡겨오게됨
    #on_delete=models.CASCADE : Question(질문) 항목 삭제 시 관계된 선택지들도 모두 자동 삭제
    choice_text = models.CharField(max_length=200)# 설문조사 주제에 대한 선택지 텍스트
    votes = models.IntegerField(default=0)#해당 선택지의 득표 수
    def __str__(self):
        return self.choice_text