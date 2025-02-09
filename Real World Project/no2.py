import smtplib

def send_email(subject, body, to_email):
    server = smtplib.SMTP('', 587)
    server.starttls()
    server.login('your_email', 'your_password')
    message = f"Subject: {subject}\n\n{body}"
    server.sendmail('your_email', to_email, message)
    server.quit()
