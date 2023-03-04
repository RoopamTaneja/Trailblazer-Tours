from django.db import models
from tour.models import Tour

class Question(models.Model):
    trip = models.ForeignKey(Tour, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    ques_type = models.CharField(max_length=100,default="Other")

    def __str__(self):
        return self.question_text



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    new_id = models.CharField(max_length= 50, default="")
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
