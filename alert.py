import smtplib
from email.mime.text import MIMEText
from config import ALERT_EMAIL, SMTP_SERVER, SMTP_PORT, EMAIL_USER, EMAIL_PASS

def send_alert(metrics):
    subject = "⚠️ High Resource Usage Alert!"
    body = f"CPU Usage: {metrics['cpu_usage']}%\nMemory Usage: {metrics['memory_usage']}%"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_USER
    msg["To"] = ALERT_EMAIL

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)
        server.sendmail(EMAIL_USER, ALERT_EMAIL, msg.as_string())
        server.quit()
        print("Alert sent successfully!")
    except Exception as e:
        print(f"Error sending alert: {e}")
