import  smtplib

from email.mime.text import MIMEText
from email.header import Header

sender = '863064604@qq.com'
receivers = ['18338671101@163.com']


message = MIMEText('测试','plain','utf-8')
message['From'] = Header('python','utf-8')
message['To'] = Header('测试','utf-8')
subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender,receivers,message.as_string())
    print('发送成功')
except smtplib.SMTPException:
    print('邮件发送失败')