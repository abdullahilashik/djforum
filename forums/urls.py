from django.urls import path
from .views import (
    QuestionListView,
    QuestionDetailsView,
    TopicListview,
    TopicCreateView,
    TopicDeleteView
)

app_name = 'forums'
urlpatterns = [
    path('', TopicListview.as_view(), name='topic-list'),
    path('topic/<slug:topic>/', QuestionListView.as_view(), name='question-list'),
    path('topic/<slug:topic>/question/<slug:slug>/', QuestionDetailsView.as_view(), name='question-slug'),
    path('topic-create/', TopicCreateView.as_view(), name='topic-create'),
    path('topic-delete/<int:pk>', TopicDeleteView.as_view(), name='topic-delete')
]
