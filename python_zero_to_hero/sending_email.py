import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

email = EmailMessage()

email['from'] = '8314home@gmail.com'
email['to'] = '8314home@gmail.com'
email['subject'] = 'A test email'

html_index_file = Path('src/index.html').read_text()
html_text_message = Template(html_index_file,).safe_substitute(name='8314home')  # Template type allows substitution
email.set_content(html_text_message, 'html')

email.add_attachment(open('src/watermarked_pdf.pdf', 'rb').read(), maintype='application/pdf',
                     subtype='pdf', filename='watermarked_pdf.pdf')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp_conn:
    smtp_conn.ehlo()
    smtp_conn.starttls() # to make comm secure
    smtp_conn.login('8###home@gmail.com', '######') # replace password
    smtp_conn.send_message(email)
    print("Sent mail")

