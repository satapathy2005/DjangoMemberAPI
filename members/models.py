from django.db import models
from  django.core.exceptions import ValidationError

def validate_role(value):
    if not (value == 'regular' or value == 'admin'):
        raise ValidationError(value + ' is not a valid role')


class Member(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email_address = models.CharField(max_length=200, unique=True)
    phone_number = models.CharField(max_length=20, unique=True)
    role = models.CharField(validators=[validate_role], max_length=8)

    def update(self, new_values):
        for key in new_values:
            if key == "first_name":
                self.first_name = new_values[key]
            elif key == "last_name":
                self.last_name = new_values[key]
            elif key == "email_address":
                self.email_address - new_values[key]
            elif key == "phone_number":
                self.phone_number = new_values[key]
            elif key == "role":
                self.role = new_values[key]
            else:
                return "bad key given"
        self.save()

    def __str__(self):
        return self.first_name + "-" + self.last_name


