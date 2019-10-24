from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from django_extensions.db.fields import AutoSlugField


class QuestionManager(models.Manager):
    """ Custom Manager """

    def all(self):

        return Question.objects.filter(approved_question=True)

    def pending_approval(self):

        return super().get_queryset().filter(approved_question=False)


class Question(models.Model):
    """ Question Models """

    title = models.CharField(_('Title'), max_length=200)
    body = models.TextField(_('Content'), blank=True, null=True)
    slug = AutoSlugField(_('Slug'), populate_from=['title', ])
    approved_question = models.BooleanField(_('Active'), default=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               null=True,
                               on_delete=models.CASCADE,
                               related_name='questions',
                               verbose_name=_('Author')
                               )
    start_date = models.DateTimeField(_('Onlince since'), blank=True, null=True)
    end_date = models.DateTimeField(_('End date'), blank=True, null=True)
    created_at = models.DateTimeField(_('Create date'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Update date'), auto_now=True)

    class Meta:

        verbose_name = 'Question Manager'
        verbose_name_plural = 'Questions Manager'

    def approve(self):

        self.approved_question = True
        self.save()

    def __str__(self):

        return self.title

    objects = QuestionManager()  # Custom manager
