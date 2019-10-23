from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from django_extensions.db.fields import AutoSlugField


class Question(models.Model):
    """ Question Models """

    title = models.CharField(_('Title'), max_length=200)
    body = models.TextField(_('Content'), blank=True, null=True)
    slug = AutoSlugField(_('Slug'), populate_from=['title', ])
    active = models.BooleanField(_('Active'), default=False)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,
                                   on_delete=models.CASCADE, related_name='questions',
                                   verbose_name=_('Author')
                                   )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
