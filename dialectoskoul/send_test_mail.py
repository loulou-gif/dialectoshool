from django.core.mail import send_mail

send_mail(
    subject='Test depuis Django',
    message='Ceci est un message de test',
    from_email='konankanjulius10@gmail.com',
    recipient_list=['konankanjulius10@gmail.com'],
    fail_silently=False
)
