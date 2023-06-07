# Django
from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):

    category_name = models.CharField(max_length=255, default="Has no category", verbose_name=_("Category"))

    def __str__(self):
        return self.category_name


class Lesson(models.Model):

    class Meta:
        verbose_name = _("Lesson")
        verbose_name_plural = _("Lessons")
        ordering = ['id']

    SCALE = (
        (1, _('Beginner')),
        (2, _('Intermediate')),
        (3, _('Advance'))
    )

    lesson_title = models.CharField(max_length=255, blank=False, null=False, verbose_name=_("Lesson Title"))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_("Lesson Category"))
    difficulty = models.IntegerField(choices=SCALE, default=1, verbose_name=_("Difficulty"))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_("Date Created"))
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.lesson_title


class Content(models.Model):

    class Meta:
        verbose_name = "Content" # "Content"
        verbose_name_plural = "Contents"
        ordering = ['id']

    related_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name=_("Related Lesson"))
    video_url = models.URLField(max_length=512, verbose_name=_("Video URL"))
    content_header = models.CharField(max_length=255, verbose_name=_("Content Header"))
    content_text = models.TextField(verbose_name=_("Content Text"))

    def __str__(self):
        return self.content_header


class Conference(models.Model):

    class Meta:
        verbose_name = _("Conference")
        verbose_name_plural = _("Conferences")
        ordering = ['id']

    conference_topic = models.CharField(max_length=255, verbose_name=_("Conference Topic"))
    related_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name=_("Related Lesson"))
    conference_url = models.URLField(max_length=512, verbose_name=_("Conference URL"))

    def __str__(self):
        return self.conference_topic
