from django.shortcuts import render, reverse
from .models import Question, Topic
from django.views import generic
from .forms import TopicForm


class QuestionListView(generic.ListView):
    template_name = 'forum/question-list.html'
    # queryset = Question.objects.all()
    context_object_name = 'questions'

    def get_queryset(self):
        queryset = Question.objects.filter(topic__slug=self.kwargs['topic'])
        return queryset


class QuestionDetailsView(generic.DetailView):
    template_name = 'forum/question-details.html'
    slug_field = 'slug'
    queryset = Question.objects.all()
    context_object_name = 'question'


class TopicListview(generic.ListView):
    template_name = 'forum/topic-list.html'
    queryset = Topic.objects.all()
    context_object_name = 'topics'


class TopicCreateView(generic.CreateView):
    template_name = 'forum/topic-create.html'
    queryset = Topic.objects.all()
    form_class = TopicForm

    def get_success_url(self):
        return reverse('forums:topic-list')


class TopicDeleteView(generic.DeleteView):
    template_name = 'forum/topic-delete.html'
    queryset = Topic.objects.all()
    context_object_name = 'topic'

    def get_success_url(self):
        return reverse('forums:topic-list')
