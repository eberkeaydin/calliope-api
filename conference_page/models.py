# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Conference
from lesson.models import Conference


class ConferencePage(models.Model):


    class Meta:
        verbose_name = _("Conference Page")
        verbose_name_plural = _("Conference Pages")
        ordering = ['id']


    # SURVEY_ANSWERS = (
    #     (1, _('Very few')),
    #     (2, _('Fewer')),
    #     (3, _('Normal')),
    #     (4, _('Pretty')),
    #     (5, _('Excessive'))
    # )

    related_conference = models.ForeignKey(Conference, null=True, on_delete=models.CASCADE, verbose_name=_("Related Conference"))
    code_editor_url = models.URLField(max_length=512, verbose_name=_("Code Editor URL"))
    # survey_question = models.CharField(max_length=512, verbose_name=("Survey Question"))
    # survey_answer = models.IntegerField(choices=SURVEY_ANSWERS, default=3, verbose_name=("Survey Answer"))
    directive_text = models.TextField(default='', verbose_name=_("Directives"))
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.code_editor_url
