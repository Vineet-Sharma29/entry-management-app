import os
import boto3

# Create an SNS client
sns = boto3.client(
        'sns',
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
        region_name=os.getenv("AWS_REGION_NAME")
    )

# Send a SMS message to the specified phone number
def check_in_sms(host_name, visitor_name, visitor_check_in, host_phone_no):
    sns.publish(
        PhoneNumber=host_phone_no,
        Message='Hi, {} you have a meeting with {} at {}!'.format(host_name, visitor_name, visitor_check_in),
    )