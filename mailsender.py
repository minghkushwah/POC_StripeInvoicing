import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(to_email, invoice_url, amount, description):
    
    try:
        # Get the invoice URL
        #invoice_url = f"https://dashboard.stripe.com/invoices/{invoice_id}"

        # Compose the email
          # Email body
        body = f"""
        <h2>Invoice Details</h2>
        <p>Thank you for your business. Here are the details of your invoice:</p>
        <ul>
            <li>Description: {description}</li>
            <li>Amount: {amount} USD</li>
        </ul>
        <p>You can view and pay the invoice using the following link:</p>
        <a href="{invoice_url}">Pay Invoice</a>
        <p>Thank you for your prompt payment.</p>
        """

        msg = MIMEMultipart()
        msg['From'] = 'noreply@veersatech.com'
        msg['To'] = to_email
        msg['Subject'] = 'Your Invoice from Our Company'

        msg.attach(MIMEText(body, 'html'))
       
         # SMTP server setup
        smtp_server = "smtp-mail.outlook.com"
        smtp_port = 587
        smtp_password = "vTrack@20236"
         
        # Send the email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login('noreply@veersatech.com', smtp_password)
        server.sendmail(to_email, to_email, msg.as_string())
        
        print(f"Email sent successfully to {to_email}")

    except Exception as e:
        print(f"Failed to send email: {e}")
    finally:
    # Quit the server connection
       server.quit()


#send_email('Madhusudan@veersatech.com','123456',100,'test Invoice')