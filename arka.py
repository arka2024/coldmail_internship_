import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Gmail credentials
sender_email = "abcd@gmail.com"
password = "fdbrifnr"  # Use an app password for Gmail

# List of recipient emails
# receiver_emails = [
#    
# ] # Add more emails as needed


# Path to your resume file
resume_path =  "C:\\Users\\KIIT0001\\Downloads\\Aryan_Resume (2).pdf" # Change this to your actual resume file path

# Email body with HTML formatting
html_content = """  
<html>
<head>
    <style>
        body, p, li, b, strong, a, span {
            font-family: Arial, sans-serif; 
            color: black !important;  /* Forces all text to black */
            text-decoration: none;  /* Removes underlines from links */
        }
    </style>
</head>
<body>
    <p>Good Afternoon, </p>
</body>
</html>
"""

# Ensure resume file exists
if not os.path.exists(resume_path):
    print("Resume file not found!")
else:
    # Send email to each recipient
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()  # Secure the connection
        server.login(sender_email, password)

        for receiver_email in receiver_emails:
            msg = MIMEMultipart()
            msg["From"] = sender_email
            msg["To"] = receiver_email
            msg["Subject"] = "INTERNSHIP APPLICATION || INVEST INDIA || ARYAN BHARGAVA"

            # Attach the HTML content
            msg.attach(MIMEText(html_content, "html"))

            # Attach the resume file
            with open(resume_path, "rb") as resume_file:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(resume_file.read())

            encoders.encode_base64(part)  # Encode the file
            part.add_header("Content-Disposition", f"attachment; filename={os.path.basename(resume_path)}")
            msg.attach(part)  # Attach file to email

            # Send the email
            server.sendmail(sender_email, receiver_email, msg.as_string())
            print(f"Email sent successfully to {receiver_email}!")

        server.quit()
    except Exception as e:
        print(f"Error: {e}")
