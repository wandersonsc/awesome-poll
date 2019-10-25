from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from choices.models import Choice


class Answer(models.Model):
    """ Asnwer Model """

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name='answers',
                             verbose_name=_('User')
                             )
    choice = models.ForeignKey(Choice,
                               on_delete=models.CASCADE,
                               related_name='answer_choices',
                               verbose_name=_('Choice')
                               )
    answer = models.CharField(_('Answer'), max_length=200, unique=True)
    created_at = models.DateTimeField(_('Create date'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Update date'), auto_now=True)

    class Meta:

        ordering = ['-created_at']
        verbose_name = 'Asnwer Manager'
        verbose_name_plural = 'Asnwers Manager'

    def __str__(self):

        return self.answer
