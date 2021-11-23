from django import forms
from .models import Topic, Question, Answer


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = '__all__'
