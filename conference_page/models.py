# Django
from django.db import models
from django.utils.translation import gettext_lazy as _


class ConferencePage(models.Model):


    class Meta:
        verbose_name = _("Conference Page")
        verbose_name_plural = _("Conference Pages")
        ordering = ['id']

    code_editor_url = models.URLField(max_length=512, verbose_name=_("Code Editor URL"))
    directive_header = models.CharField(default='Directives', max_length=255, verbose_name=_("Directives Header"))
    directive_text = models.TextField(default='', verbose_name=_("Directives"))
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.directive_header


class SurveyQuestion(models.Model):


    class Meta:
        verbose_name = _("Survey")
        verbose_name_plural = _("Surveys")
        ordering = ['id']

    survey_question = models.CharField(max_length=512, verbose_name=("Survey Question"))
    is_active = models.BooleanField(default=True, verbose_name=_("Active Status"))

    def __str__(self):
        return self.survey_question


class SurveyAnswer(models.Model):


    class Meta:
        verbose_name = _("Survey Answer")
        verbose_name_plural = _("Survey Answers")
        ordering = ['id']

    SURVEY_ANSWERS = (
        (1, _('Very few')),
        (2, _('Fewer')),
        (3, _('Normal')),
        (4, _('Pretty')),
        (5, _('Excessive'))
    )

    related_survey = models.ForeignKey(SurveyQuestion, related_name='related_survey', on_delete=models.CASCADE)
    survey_answer = models.IntegerField(choices=SURVEY_ANSWERS, default=3, verbose_name=("Survey Answer"))
    is_active = models.BooleanField(default=True, verbose_name=_("Active Status"))

    def __int__(self):
        return self.survey_answer
