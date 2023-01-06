import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import auth_data


class Email():
    def __init__(self, login, password):
        self.login = login
        self.password = password

    def send_message(self, subject, recipients, message):
        GMAIL_SMTP = "smtp.gmail.com"
        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message))

        msg_send = smtplib.SMTP(GMAIL_SMTP, 587)
        # identify ourselves to smtp gmail client
        msg_send.ehlo()
        # secure our email with tls encryption
        msg_send.starttls()
        # re-identify ourselves as an encrypted connection
        msg_send.ehlo()
        msg_send.login(self.login, self.password)
        msg_send.sendmail(self.login, msg['To'], msg.as_string())

        msg_send.quit()
        return "send end"

    def recieve(self, header=None):
        GMAIL_IMAP = "imap.gmail.com"
        mail = imaplib.IMAP4_SSL(GMAIL_IMAP)
        mail.login(self.login, self.password)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = mail.uid('search', None, criterion)

        assert data[0], 'There are no letters with current header'

        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_bytes(raw_email)

        mail.logout()
        print('end recieve')

        return email_message


def main():
    mailman = Email(login=auth_data.gmail_login, password=auth_data.gmail_password)

    subject = 'Subject'
    recipients = ['vasya@email.com', 'petya@email.com']
    message = 'Message'
    header = None

    print(mailman.send_message(subject=subject, recipients=recipients, message=message))
    print(mailman.recieve(header=header))


if __name__ == '__main__':
    main()
