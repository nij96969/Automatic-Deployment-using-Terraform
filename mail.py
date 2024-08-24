import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email(sender_email, sender_app_password, receiver_email, subject, body, attachment_path):
    # Set up the SMTP server
    smtp_server = 'smtp.gmail.com'  # Gmail SMTP server
    smtp_port = 587  # Port for TLS

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject
    
    # Add body to email
    message.attach(MIMEText(body, 'plain'))
    
    # Open the file to be sent
    attachment = open(attachment_path, "rb")
    
    # Add attachment to email
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % attachment_path.split("\\")[-1])
    
    # Attach the attachment to the message
    message.attach(part)
    
    # Connect to SMTP server and send email
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_app_password)
    text = message.as_string()
    server.sendmail(sender_email, receiver_email, text)
    server.quit()
    print("Email sent successfully!")

#https://myaccount.google.com/apppasswords?pli=1&rapt=AEjHL4MfbyeNzEQ4DaWPFryxUlPhQ2FtP2DUgEFM9ov_An5fLrfkF8mc5gErryStTIQJPlLy7o8QTLagRgaPTIm_vqFZ5Gd9CHY1itzVQ9kUBS-9mEALr9E