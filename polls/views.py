from django.shortcuts import render, get_object_or_404, redirect 
from django.http import HttpResponse, Http404
from .models import Question

# Create your views here.
def index(request):
    # order_by('-pub_date')[:5] : 등록 날짜 기준 내림차순 정렬 후 앞에서 5개까지만
    #Question 테이블의 pub_date 순서대로 꺼냄. objects(테이블의 row)를 꺼냄. 
    latest_question_list = Question.objects.order_by('-pub_date')[:5] 
    # 지난 실습에서 render() 함수의 {~:~} 로 html 파일에게 넘겨주던 dict를 context라고 부릅니다.
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    # list(QuerySet)가 return될 시에는 get_object_or_404 대신 get_list_or_404를 활용
    q=get_object_or_404(Question, id=question_id)
    #get_object_or404 : id객체가 존재하지 않을 때 Http404 예외를 발생시키는것
    # try:
    #     q = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Question{}does not exist'.format(question_id))#괄호안에 힌트메시지 뜨게함
    return render(request, 'polls/detail.html', {'question':q})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # print(request.POST)
    # return HttpResponse('vote')
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice_select'])
        # request.POST['choice_select'] :
        # detail.html의 <input type="radio" name="choice_select" value="{{ choice.id }}">에서 날라온 값
        # form으로 제출된 POST Request 전체에서 'choice_select'가 name인 HTML 태그의 value를 꺼내는 코드
        # request.POST 는 {~~~, 'choice_select':7} 와 같은 dictionary 형태
    except:
        # request.POST['choice_select']값이 없을 경우, error_message를 가지고 details.html로 되돌아감
        context = {'question': question, 'error_message': "You didn't select a choice."}
        return render(request, 'polls/detail.html', context)
    else: # try 문에서 에러가 발생하지 않았을 경우 마지막에 실행됩니다.
        selected_choice.votes += 1
        selected_choice.save() # 실제 DB 저장
        return redirect('polls:results', question_id=question.id)
#상대 경로: polls 앱의 results라는 이름을 가진 url로 이동
    print(request.POST)

    #request.POST['dev_passthrough']
    response = "You're voting on question{}."
    return HttpResponse(response.format(question_id))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/result.html', {'question': question})