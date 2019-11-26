from celery import task
from celery.utils.log import get_task_logger
from .api.email_api import check_out_email

logger = get_task_logger(__name__)


@task(name="send_check_out_email")
def send_check_out_email(host_name, visitor_name, visitor_phone_no, visitor_email, visitor_check_in, visitor_check_out):
    """send an email when visitor checks out"""
    logger.info("check-out email send")
    check_out_email(host_name, visitor_name, visitor_phone_no, visitor_email, visitor_check_in, visitor_check_out)
