from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import UserLoginView, quiz_list, attempt_quiz, view_score

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('quizzes/', quiz_list, name='quiz_list'),
    path('quizzes/<int:quiz_id>/', attempt_quiz, name='attempt_quiz'),
    path('score/<int:attempt_id>/', view_score, name='view_score'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
