import smtplib
from email.message import EmailMessage
import imghdr
import re

smtp_server='smtp.gmail.com'
smtp_port=465

def sendEmail(addr):
	reg='^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$'
	if bool (re.match(reg,addr)):
		smtp.send_message(message)
		print('정상적으로 메일이 발송되었습니다.')
	else:
		print('유효한 이메일 주소가 아닙니다.')

message=EmailMessage()
message.set_content('코드라이언 메일 수업 중')

message['Subject']='제목입니다.'
message['From']='happine2s@likelion.org'
message['To']='ha2pine2s@gmail.com'

image=open('codelion.png','rb')
with open('codelion.png','rb') as image:
	imgfile=image.read()

message.add_attachment(imgfile,maintype='image',subtype=imghdr.what('codelion',imgfile))

smtp=smtplib.SMTP_SSL(smtp_server,smtp_port)
smtp.login('happine2s@likelion.org','')
sendEmail('happine2s@gmail.com')

#print(os.environ.get("EMAIL_USER")) 
#smtp.send_message(message)
#smtp.quit()
