from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta

# Create your models here.
class Question(models.Model):
    question_text = models.CharField('内容',max_length=200)
    pub_date = models.DateTimeField('发布时间')

    def __str__(self):      
        return self.question_text

    def was_published_recently(self):
        if timezone.now() - timedelta(days=1) <= self.pub_date:
            return True
        else:
            return False

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField('选项内容', max_length=200)
    votes = models.IntegerField('投票数', default=0)

    def __str__(self):
        return self.choice_text
