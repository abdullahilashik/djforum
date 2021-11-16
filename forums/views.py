from django.shortcuts import render
from .models import Question, Topic
from django.views import generic


class QuestionListView(generic.ListView):
    template_name = 'forum/question-list.html'
    queryset = Question.objects.all()
    context_object_name = 'questions'


class QuestionDetailsView(generic.DetailView):
    template_name = 'forum/question-details.html'
    slug_field = 'slug'
    queryset = Question.objects.all()
    context_object_name = 'question'
