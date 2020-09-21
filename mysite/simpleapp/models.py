from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
class Question(models.Model):
    question_text=models.CharField(max_length=50)
    pub_date=models.DateTimeField('date pub')

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"

    def __str__(self):
        return self.question_text

    

class Choice(models.Model):

    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)

    class Meta:
        verbose_name = "Choice"
        verbose_name_plural = "Choices"

    def __str__(self):
        return self.question
