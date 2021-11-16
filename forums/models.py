from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Topic(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']


class Question(models.Model):
    STATUS_CHOICES = (
        ('success', 'Active'),
        ('info', 'Suspended'),
        ('red', 'Spam'),
        ('primary', 'Solved')
    )
    title = models.CharField(max_length=400)
    description = models.TextField()
    slug = models.SlugField(max_length=250)
    tags = models.CharField(max_length=500)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=250, choices=STATUS_CHOICES)
    views = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']


class Answer(models.Model):
    answer = models.CharField(max_length=500)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.answer

    class Meta:
        ordering = ['-created']
