from django.contrib import admin

from my_app.models import Quiz, Question, Choice, Attempt


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('name', 'creator')
    search_fields = ('name', 'creator')
    list_filter = ('name', 'creator')


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'quiz',)
    search_fields = ('quiz', 'text')
    list_filter = ('quiz', 'text')


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('text', 'question', 'is_correct')
    list_filter = ('question', 'is_correct')
    search_fields = ('question', 'text')


@admin.register(Attempt)
class AttemptAdmin(admin.ModelAdmin):
    list_display = ('student', 'quiz', 'score')
    list_filter = ('quiz', 'student')
    search_fields = ('quiz', 'student')
