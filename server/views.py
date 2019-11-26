# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.generics import CreateAPIView
from .serialisers import MeetingSerialiser

# Create your views here.

# View to create meetings
class Meeting(CreateAPIView):
    serializer_class = MeetingSerialiser
