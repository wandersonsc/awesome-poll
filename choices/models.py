from django.db import models
from django.utils.translation import gettext_lazy as _

from polls.models import Question


class Choice(models.Model):
    """ Choice Model """

    text = models.TextField(_('Title'))
    question = models.ForeignKey(Question,
                                 on_delete=models.CASCADE,
                                 related_name='choices',
                                 verbose_name=_('Choices')
                                 )
    created_at = models.DateTimeField(_('Create date'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Update date'), auto_now=True)

    class Meta:

        unique_together = ['question', 'text']
        ordering = ['-created_at']

    def __str__(self):

        return self.title
