from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

User = get_user_model()


class UserCreateForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2'
        )

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Diplay Name'
        self.fields['email'].label = 'Email Address'

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    def clean_email(self):
        # custom validation for the email field

        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email).exists()

        if qs:
            raise ValidationError('Email already exists.')

        return email
