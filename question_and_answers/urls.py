# type: ignore
from django.urls import path
from question_and_answers.views import (
    QuestionListView,
    post_question_view,
    view_question_view,
    post_answer_view,
    like_answer_view,
)

urlpatterns = [
    path("questions/", QuestionListView.as_view(), name="question_list"),
    path("questions/post/", post_question_view, name="post_question"),
    path("questions/<int:question_id>/", view_question_view, name="view_question"),
    path(
        "questions/<int:question_id>/answer/",
        post_answer_view,
        name="post_answer",
    ),
    path("answers/<int:answer_id>/like/", like_answer_view, name="like_answer"),
]
