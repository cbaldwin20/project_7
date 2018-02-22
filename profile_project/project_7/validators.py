from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
import re

class LowerAndUpperValidator:
    # the validate method is used to test the password
    def validate(self, password, user=None):
        lower = re.compile(r'[a-z]')
        upper = re.compile(r'[A-Z]')
        has_lower = lower.search(password)
        if has_lower is None:
            raise ValidationError(
                'The password must include at least one lowercase \
                letter',
                code='password_no_lower'
            )
        has_upper = upper.search(password)
        if has_upper is None:
            raise ValidationError(
                'The password must include at least one uppercase \
                letter',
                code='password_no_upper'
            )

    # the get_help_text method is used to add a help message to the
    # password field's help texts
    def get_help_text(self):
        return ('Your password must include at least one lowercase ' 
            'and one uppercase letter')


class AtLeastOneValidator:

    def __init__(self, min_length=1):
        self.min_length = min_length

    def validate(self, password, user=None):
        special_characters = "[~\!@#\$%\^&\*\(\)_\+{}\":;'\[\]]"
        if not any(char.isdigit() for char in password):
            raise ValidationError(_('Password must contain at least'
                ' %(min_length)d digit.') % {
                                    'min_length': self.min_length})
        
        if not any(char.isalpha() for char in password):
            raise ValidationError(_('Password must contain at '
                'least %(min_length)d letter.') % {
                                    'min_length': self.min_length})
        
        if not any(char in special_characters for char in password):
            raise ValidationError(_('Password must contain at '
                'least %(min_length)d special character.') % {
                                    'min_length': self.min_length})

    def get_help_text(self):
        return "Your password must contain at least one letter, \
                            number, and special character."


class NoUsername:
    """ when a user is registering, their password can't have their
    username inside of it"""
    def validate(self, password, user=None):
        username = user.username.lower()
        if username in password.lower():
            raise ValidationError("The new password cannot contain your "
                "username ({})".format(username))

    def get_help_text(self):
        return "Your password cannot contain your username."
