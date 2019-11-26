# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.validators import validate_email, RegexValidator
import uuid

# validators for phone_no, name
phone_no_only = RegexValidator(
    regex='^[+0-9]',
    message='Please enter digits only in mobile number',
    code='phone_no_only',
)

alpha_space = RegexValidator(
    regex='^[a-zA-Z ]+$',
    message='Please enter alphabets and space only in your full name',
    code='alpha_space'
)


# Model for Host
class Host(models.Model):
    host_id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50, validators=[alpha_space])
    email = models.EmailField(validators=[validate_email])
    phone_no = models.CharField(max_length=13, validators=[phone_no_only])

    def __str__(self):
        return self.name


# Model for visitor
class Visitor(models.Model):
    visitor_id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50, validators=[alpha_space])
    email = models.EmailField(validators=[validate_email])
    phone_no = models.CharField(max_length=13, validators=[phone_no_only])
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    meeting_host = models.ForeignKey(Host, on_delete=models.CASCADE, related_name='visitor')

    def __str__(self):
        return self.name
