from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class ComplexityValidator:
    def validate (self, password, user=None):
        minimum_req = 1
        washington_capitals = [char for char in password if char.isupper()]
        lowers =[char for char in password if char.islower()]
        numbers = [char for char in password if char.isdigit()]
        special = [char for char in password if not char.isalnum()]

        if(len(washington_capitals) < minimum_req or
           len(lowers) < minimum_req or
           len(numbers) < minimum_req or
           len(special) < minimum_req ):
            raise ValidationError(
                _("You need at least one uppercase letter, one lowercase letter, one number, one non-word character!"),
                code="You need at least one uppercase letter, one lowercase letter, one number, one non-word character."
            )


class CharacterRepeatValidator:
    def validate(self, password, user=None):
        for char in password:
            if char * 3 in password:
                raise ValidationError(_("You may not repeate one character two times in a row."), code="You may not repeate one character two times in a row.")