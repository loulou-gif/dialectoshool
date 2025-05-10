from django.core.mail import send_mail
from django.utils import timezone
from .models import *

def serviceSendEmail(email_obj):
    try:
        send_mail(
            subject=email_obj.subject,
            message=email_obj.message,
            recipient_list=[email_obj.to_email],
            from_email=email_obj.from_email,
            fail_silently=False,
        )
        email_obj.is_sent = True
        email_obj.sent_at = timezone.now()
        email_obj.save()
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False
    
