from django.urls import path
from .views import (
    QuestionListView,
    QuestionDetailsView,
    TopicListview
)

app_name = 'forums'
urlpatterns = [
    path('', TopicListview.as_view(), name='topic-list'),
    path('questions/<slug:topic>/', QuestionListView.as_view(), name='question-list'),
    path('<slug:slug>/', QuestionDetailsView.as_view(), name='question-slug')
]
