from .models import Host, Visitor
from rest_framework import serializers
from datetime import datetime
from .api.email_api import check_in_email
from .tasks import send_check_out_email
from .api.sms_api import check_in_sms


# visitor-serialise will serialise visitor model
class VisitorSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Visitor
        fields = ['name', 'email', 'phone_no', 'check_in', 'check_out']


# meeting serialiser which will add host and visitor as well as will call email and sms api
class MeetingSerialiser(serializers.ModelSerializer):
    # since foreign key attribute is used in visitor model therefore it needs to be serialised in a nested manner
    visitor = VisitorSerialiser(many=True)

    class Meta:
        model = Host
        fields = ['name', 'email', 'phone_no', 'visitor']

    # following create method will override create method of ModelSerializer
    def create(self, validated_data):
        visitor_data = validated_data.pop('visitor')
        host = Host.objects.create(**validated_data)
        visitor = Visitor.objects.create(meeting_host=host, **visitor_data[0])
        check_in_email(host.name, visitor.name, datetime.now().strftime("%d %b, %Y - %H:%M"), host.email)
        check_in_sms(host.name, visitor.name, visitor.check_in.strftime("%d %b, %Y - %H:%M"), host.phone_no)
        send_check_out_email.apply_async(
            args=[host.name, visitor.name, visitor.phone_no, visitor.email, visitor.check_in, visitor.check_out],
            eta=(visitor.email))
        return host
