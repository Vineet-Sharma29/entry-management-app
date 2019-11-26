from django.core.mail import send_mail

# api to send email when visitor checks in
def check_in_email(host_name, visitor_name, check_in, visitor_email):
    send_mail('Meeting',
              'Hi, {} you have a meeting with {} at {}'.format(host_name, visitor_name, check_in),
              'ems@ems.com',
              [visitor_email],
              fail_silently=False)

# api to send email when user checks out
def check_out_email(host_name, visitor_name, visitor_phone_no, visitor_email, visitor_check_in, visitor_check_out):
    send_mail('Thanks!',
              '{}, it was pleasure having your company with us. We may contact you at {} for any query in future. \nWarm Regards, {}.\n\n You checked in at {} and your check out time is {}'.format(
                  visitor_name, visitor_phone_no, host_name, visitor_check_in, visitor_check_out),
              'ems@ems.com',
              [visitor_email],
              fail_silently=False)
