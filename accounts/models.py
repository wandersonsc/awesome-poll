from django.conf import settings
from django.contrib import auth
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):

        return self.username


class Profile(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                verbose_name=_('User')
                                )
    country = models.CharField(_('Country'), max_length=30, blank=True, default="US")
    age = models.PositiveIntegerField(_('Age'), default=0)
    city = models.CharField(_('City'), max_length=100, blank=True, default="None")
    last_login = models.DateTimeField(_('Last login'), auto_now_add=True)
    created_at = models.DateTimeField(_('Create date'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Update date'), auto_now=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('accounts:detail_profile', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Profiles Manager'
        verbose_name_plural = 'Profiles Manager'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
