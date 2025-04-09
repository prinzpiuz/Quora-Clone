# type: ignore
from django.views.generic import ListView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from question_and_answers.models import Question, Answer, Like
from question_and_answers.forms import QuestionForm, AnswerForm


class QuestionListView(ListView):
    model = Question
    template_name = "home.html"


@login_required
def post_question_view(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            messages.success(request, "Question posted successfully!")
            return redirect("question_list")
    else:
        form = QuestionForm()
    return render(request, "post_question.html", {"form": form})


@login_required
def view_question_view(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    answer_form = AnswerForm()
    return render(
        request,
        "view_question.html",
        {"question": question, "answer_form": answer_form},
    )


@login_required
def post_answer_view(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.author = request.user
            answer.save()
            messages.success(request, "Answer posted successfully!")
            return redirect("view_question", question_id=question_id)
    return redirect("view_question", question_id=question_id)


@login_required
def like_answer_view(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    like, created = Like.objects.get_or_create(answer=answer, user=request.user)
    if not created:
        like.delete()
    return HttpResponseRedirect(
        reverse("view_question", kwargs={"question_id": answer.question.id})
    )
