# Django
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(models.Model):

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        ordering = ['id']

    ROLES = (
        (0, _('No role')),
        (1, _('Learner')),
        (2, _('Tutor'))
    )

    user_name = models.CharField(max_length=65, default="username", unique=True, verbose_name=_("User name"))
    role = models.IntegerField(choices=ROLES, default=0, verbose_name=_("Role"))
    score = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_("Date Created"))
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.user_name
