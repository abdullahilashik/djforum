from django.urls import path
from .views import (
    QuestionListView,
    QuestionDetailsView
)

app_name = 'forums'
urlpatterns = [
    path('', QuestionListView.as_view(), name='question-list'),
    path('<slug:slug>/', QuestionDetailsView.as_view(), name='question-slug')
]
