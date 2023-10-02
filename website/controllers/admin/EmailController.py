import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(to_email, subject, message):
    smtp_server = 'smtp.office365.com'  # Înlocuiți cu serverul SMTP real
    smtp_port = 587  # Portul pentru serverul SMTP (587 pentru TLS, 465 pentru SSL)
    smtp_username = 'rebejanicolae@gmail.com'  # Înlocuiți cu numele de utilizator pentru autentificarea SMTP
    smtp_password = 'gjhtpbrgujdfayir'  # Înlocuiți cu parola pentru autentificarea SMTP

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
