# https://testdriven.io/blog/django-custom-user-model/

from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Manager for a custom User model.
    The default User model in Django has usernames for authentication,
    whereas teldrassil instead uses emails.
    """
    def create_user(self, email, first_name, last_name, password, **kwargs):
        if email is None:
            raise ValidationError(_('email must not be blank.'))
        if first_name is None:
            raise ValidationError(_('first name must not be blank.'))
        if last_name is None:
            raise ValidationError(_('last name must not be blank.'))
        if password is None:
            raise ValidationError(_('password must not be blank.'))

        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            **kwargs)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, first_name, last_name, password, **kwargs):
        kwargs.setdefault('is_active', True)
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)

        if kwargs.get('is_staff') is False:
            raise ValidationError(_('superuser requires is_staff=True.'))
        if kwargs.get('is_superuser') is False:
            raise ValidationError(_('superuser requires is_superuser=True.'))

        return self.create_user(email, first_name, last_name, password, **kwargs)