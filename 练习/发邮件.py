import  smtplib
from  email.mime.text import MIMEText
from   email.header import Header

#HNUGFXIKBXFSUDFU
def send_mail(email_tit,email_content,eml_to_person):
    smtp_obj = smtplib.SMTP('smtp.163.com')
    #登录邮箱
    smtp_obj.login('18338671101@163.com','HNUGFXIKBXFSUDFU')
    #发给谁
    to_person = eml_to_person
    #标题
    tit = Header(email_tit,'utf-8')
    #发送者
    sender = Header('18338671101@163.com','utf-8')
    #内容
    con = MIMEText(email_content,'html','utf-8')
    con['From'] = sender
    con["Subject"] = tit

    att1 = MIMEText(open('content.html', 'rb').read(), 'base64', 'utf-8')  # 添加附件
    att1["Content-Type"] = 'application/octet-stream'  # 设置类型
    att1["Content-Disposition"] = 'attachment; filename="{0}"'.format("test.xlsx")  # 设置邮件用现实的名称
    con.attach(att1)


    smtp_obj.sendmail('18338671101@163.com',to_person,con.as_string())
if __name__ == '__main__':
    t = '证明'
    c = '已从乾道离职'
    p = '863064604@qq.com'
    send_mail(t,c,p)

#v_yuanjinqiu@baidu.com













