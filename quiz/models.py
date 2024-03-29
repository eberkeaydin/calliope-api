# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Calliope | Lesson
from lesson.models import Lesson


class Category(models.Model):

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Quizzes(models.Model):

    class Meta:
        verbose_name = _("Quiz")
        verbose_name_plural = _("Quizzes")
        ordering = ['id']

    category = models.ForeignKey(Category, default=1, on_delete=models.CASCADE)
    related_lesson = models.ForeignKey(Lesson, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, default=_("New Quiz"), verbose_name=_("Quiz Title"))
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Updated(models.Model):

    date_updated = models.DateTimeField( verbose_name=_("Last Updated"), auto_now=True)

    class Meta:
        abstract = True


class Question(Updated):

    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")
        ordering = ['id']

    SCALE = (
        (1, _('Beginner')),
        (2, _('Intermediate')),
        (3, _('Advance'))
    )

    TYPE = (
        (0, _('Multiple Choice')),
    )

    quiz = models.ForeignKey(Quizzes, related_name='question', on_delete=models.CASCADE)
    technique = models.IntegerField(choices=TYPE, default=0, verbose_name=_("Type of question"))
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    question_text = models.TextField(default='', verbose_name=_("Question Text"))
    difficulty = models.IntegerField(choices=SCALE, default=1, verbose_name=_("Difficulty"))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_("Date Created"))
    is_active = models.BooleanField(default=True, verbose_name=_("Active Status"))

    def __str__(self):
        return self.title


class Answer(Updated):

    class Meta:
        verbose_name = _("Answer")
        verbose_name_plural = _("Answers")
        ordering = ['id']

    question = models.ForeignKey(Question, related_name='answer', on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=255, verbose_name=_("Answer Text"))
    is_right = models.BooleanField(default=True)
