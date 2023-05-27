#urls.py(url 권한위임을 하는 쪽)에서     
#path('polls/',include('polls.urls')),#127.0.0.1:8000/polls/~~~
#뒤에 있는 polls 뒤의 url을 여기다 적는 것임
from django.urls import path
from . import views # 같은 폴더 내의 views.py를 import
app_name = 'polls'
#.은 앱이름 polls(해당 파일이 있는 상위 파일이름)를 의미함
#urlpatterns = [
#    # "127.0.0.1:8000/polls/" 이후의 URL은 polls/urls.py가 handling하도록 만들 예정입니다.
#    path('', views.index, name='index'), # '127.0.0.1:8000/polls/' 를 받아내도록 만들어줄 것입니다
#    #즉 이 url은 polls까지 적힌 이후의 url입니다. 
#    path('<>')
#]

urlpatterns = [
    # "127.0.0.1:8000/polls/" 이후의 URL은 polls/urls.py가 handling하도록 만들 예정입니다.
    path('', views.index, name='index'), # '127.0.0.1:8000/polls/' 를 받아내도록 만들어줄 것입니다.
# ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]