from django.test import TestCase
from mails.tasks import send_email
from mails.models import EmailAddress, EmailTemplate


class TestEmailSendFunction(TestCase):

    def setUp(self):
        EmailTemplate.objects.create(
            title='test title',
            body='test body'
        )

    def test_email_send(self):

        address = 'bboykermo@gmail.com'

        self.assertEquals(send_email(address), 'Message was sent')
