import threading
from django.core.mail import send_mail


class EmailThread(threading.Thread):
    def __init__(
        self, subject, message, from_email, recipient_list, fail_silently=False
    ):
        self.subject = subject
        self.message = message
        self.from_email = from_email
        self.recipient_list = recipient_list
        self.fail_silently = fail_silently
        threading.Thread.__init__(self)

    def run(self):
        send_mail(
            self.subject,
            self.message,
            self.from_email,
            self.recipient_list,
            fail_silently=self.fail_silently,
        )
