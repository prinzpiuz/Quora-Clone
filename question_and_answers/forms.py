# type: ignore
from django import forms
from question_and_answers.models import Question, Answer


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["title", "question"]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Question Title"}),
            "question": forms.Textarea(attrs={"placeholder": "Your Question"}),
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ["answer"]
        widgets = {
            "answer": forms.Textarea(attrs={"placeholder": "Your Answer"}),
        }
