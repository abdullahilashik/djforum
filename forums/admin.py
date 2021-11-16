from django.contrib import admin
from .models import Topic, Question, Answer


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'created']


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'topic', 'user', 'created']


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['answer', 'user', 'question', 'created']
