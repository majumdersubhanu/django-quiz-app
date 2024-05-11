from django.contrib.auth.models import User
from django.db import models


class Quiz(models.Model):
    name = models.CharField(max_length=100)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ['name']
        verbose_name = 'Quiz'
        verbose_name_plural = 'Quizzes'
        unique_together = ('name', 'creator')


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['text']
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'
        unique_together = ('text', 'quiz')


class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['text']
        verbose_name = 'Choice'
        verbose_name_plural = 'Choices'
        unique_together = ('text', 'question')


class Attempt(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    class Meta:
        # unique_together = ('quiz', 'student')
        verbose_name = 'Attempt'
        verbose_name_plural = 'Attempts'
