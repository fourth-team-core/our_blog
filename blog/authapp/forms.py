from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (PasswordResetForm, UserChangeForm,
                                       UserCreationForm)
from django.forms import ValidationError

from .models import BlogUser


class BlogUserCreationForm(UserCreationForm):
    class Meta:
        model = BlogUser
        fields = ("first_name", "last_name", "username", "email")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].required = True


class BlogUserChangeForm(UserChangeForm):
    class Meta:
        model = BlogUser
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
        )


class EmailValidationOnForgotPassword(PasswordResetForm):
    def clean_email(self):
        """
        Check if the given email correlates with an existing user email.
        If this is not the case -> trow a proper error message.
        """
        email = self.cleaned_data["email"]
        if (
            not get_user_model()
            .objects.filter(email__iexact=email, is_active=True)
            .exists()
        ):
            raise ValidationError(
                "There is no user registered with the given email address!"
            )
        return email
