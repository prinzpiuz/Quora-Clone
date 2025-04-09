# type: ignore

from django.db import models
from django.conf import settings


class Question(models.Model):
    title = models.CharField(max_length=255)
    question = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Answer(models.Model):
    answer = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True
    )
    question = models.ForeignKey(Question, related_name="answers", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Answer by {self.author.email} to {self.question.title}"


class Like(models.Model):
    answer = models.ForeignKey(Answer, related_name="likes", on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("answer", "user")

    def __str__(self):
        return f"Like by {self.user.email} on answer to {self.answer.question.title}"
