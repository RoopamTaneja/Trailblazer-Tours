from django import forms
from tour.models import Tour
from .models import Question

class ques_updater(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']


        
