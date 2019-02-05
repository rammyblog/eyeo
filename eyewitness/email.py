from django.core.mail import EmailMessage


def send_mail_submit(name, email, subject, ):
	mail_message = ('Hi, {} '+
		'Greetings from Eyeo, Thank you for submitting the report to us.<br>Your report is currently under review,<br>'+
		'Once it has been approved another mail will be sent to you confirming that,' +
		' and the link to the post will be sent to you. <br>'+ 
		"<br>Don't forget to call 767 if its an emergency<br>"+'Thanks!')

	email = EmailMessage(
				'{} Report Submitted at Eyeo!'.format(subject), #Subject
				mail_message.format(name), #message
				'tunde@rammyblog.com.ng',
				[str(email)],
				reply_to=['tunde@rammyblog.com.ng'],
				headers={'Message-ID': 'foo'},

			)
	email.content_subtype ="html"
	mail_sent = email.send()
	return mail_sent


def send_mail_publish(name, email, subject, message, url):
	mail_message = ('Hi, {} '+
		'Greetings from Eyeo, Thank you for submitting the report to us.<br>Your report has been approved,<br>'+
		' Below is the link to the <b>post</b>. <br>'+ "<a href='127.0.0.1{}'>click here</a>" +

		"<br> Don't forget to call 767 if its an emergency<br>"+'Thanks!')

	email = EmailMessage(
				'{} Report approved at Eyeo!'.format(subject), #Subject
				mail_message.format(name, url), #message
				'tunde@rammyblog.com.ng',
				[str(email)],
				reply_to=['tunde@rammyblog.com.ng'],
				headers={'Message-ID': 'foo'},

			)
	email.content_subtype ="html"
	mail_sent = email.send()
	return mail_sent
