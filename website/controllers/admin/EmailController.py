import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(to_email, subject, message):

    # smtp_server = 'smtp.office365.com'
    # smtp_port = 587
    # smtp_username = 'itexpert.vodafone@solutions30.com'
    # smtp_password = 'XAZ08251'

    smtp_server = 'mail.idconnectitworks.eu'
    smtp_port = 465
    smtp_username = 'itexpert.vodafone@idconnectitworks.eu'
    smtp_password = 'X4sK$sAo5gw]'

    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = to_email
    msg['Subject'] = subject

    email_body = message
    msg.attach(MIMEText(email_body, 'plain'))

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Pentru conexiunea criptată TLS
            server.login(smtp_username, smtp_password)
            server.sendmail(smtp_username, to_email, msg.as_string())
        return True  # Trimitere cu succes
    except Exception as e:
        print('Eroare la trimiterea e-mailului:', str(e))
        return False  # Eroare la trimitere
