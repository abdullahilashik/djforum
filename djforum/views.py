from django.views import generic
from forums.models import Question, Topic


class HomePageView(generic.ListView):
    template_name = 'pages/home.html'
    queryset = Question.objects.all()
    context_object_name = 'questions'
