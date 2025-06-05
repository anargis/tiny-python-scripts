from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Replace with your SendGrid API key
api_key = "YOUR-API-KEY"  

class SendTestEmail:
  def __init__(self, api_key):
    self.api_key = api_key

  def send_email(self, from_email, to_email, subject, html_content):
    message = Mail(
      from_email = from_email,
      to_emails = to_email,
      subject = subject,
      html_content = html_content
    )
    
    try:
      sg = SendGridAPIClient(self.api_key)
      response = sg.send(message)
      print (f"mail sent! Status Code: {response.status_code}")
    except Exception as e:
      print(f"Error sending email: {e}")

if __name__ == "__main__":
  email_sender = SendTestEmail(api_key)
  # Replace with your validated SendGrid email: FROM-YOUR-EMAIL@gmail.com
  # Replace with your recipient email: TO-YOUR-EMAIL@gmail.com 
  email_sender.send_email("FROM-YOUR-EMAIL@gmail.com", "TO-YOUR-EMAIL@gmail.com", "Test Email", "<h1>Test Content</h1>")