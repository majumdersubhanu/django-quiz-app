from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from .models import Quiz, Choice, Attempt


class UserLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    next_page = reverse_lazy('quiz_list')


@login_required
def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quiz_list.html', {'quizzes': quizzes})


@login_required
def attempt_quiz(request, quiz_id):
    quiz = Quiz.objects.get(pk=quiz_id)
    if request.method == 'POST':
        score = 0
        for question in quiz.questions.all():
            selected_choice = request.POST.get(str(question.id))
            if selected_choice and Choice.objects.get(id=selected_choice).is_correct:
                score += 1
        attempt = Attempt.objects.create(quiz=quiz, student=request.user, score=score)
        return redirect('view_score', attempt_id=attempt.id)
    return render(request, 'attempt_quiz.html', {'quiz': quiz})


@login_required
def view_score(request, attempt_id):
    attempt = get_object_or_404(Attempt, pk=attempt_id)
    return render(request, 'score.html', {'attempt': attempt})
