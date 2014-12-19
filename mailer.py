#main method
#go through each row in CSV File
	#replace body template with correct fields
	#send email

import csv
import sys
import smtplib

# ===== USER INPUT =======#
GMAIL_LOGIN = "achauhan@princeton.edu"
GMAIL_PASSWORD = "etotheeyepie2195"
SUBJECT = "Princeton University Start-Up Career Fair"

#You need to attach a subject body .txt file
#which has a /#i#/ in place of every token that needs to be replaced,
#where i starts at 1.

#You also need to attach a CSV in which each row contains the data 
#required to send a single email. The first column (column 0) must
#contain the email address of the recepient and the rest of the columns
#must contain the replacement ith replacement token (corresponding to the ith
#replacement denotations in the body txt file.

# ===== PROGRAM ==========#
#send email method
def send_email(recipient, subject, body):
    SMTP_SERVER = 'smtp.gmail.com'
    SMTP_PORT = 587
    gmail_sender = GMAIL_LOGIN
    password = GMAIL_PASSWORD

    sender = "Advait Chauhan <achauhan@princeton.edu>"
    headers = ["From: " + sender,
               "Subject: " + subject,
               "To: " + recipient,
               "MIME-Version: 1.0",
               "Content-Type: text/txt"]
    headers = "\r\n".join(headers)

    session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)

    session.ehlo()
    session.starttls()
    session.ehlo
    session.login(gmail_sender, password)

    session.sendmail(sender, recipient, headers + "\r\n\r\n" + body)
    session.quit()

#main method
if __name__ == "__main__":

#later make this sys.argv[1])
	subject = SUBJECT

	f = open("body.txt", 'r')
	org_body = f.read()
	f.close()
	
	body = org_body
	data = open("data.csv", 'rU')
	csv_data = csv.reader(data, dialect='excel')

	for row in csv_data:
		rcpt = row[0]
		print rcpt
		for i in range (1, len(row)):
			r = "/#" + str(i) + "#/"
			body = body.replace(r, row[i])
		send_email(rcpt, subject, body)
		body = org_body



