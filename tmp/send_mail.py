import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import config

# 组装邮件正文
msg = MIMEMultipart()
body = MIMEText('python发送邮件','plain','utf-8')
msg.attach(body)

# 组装邮件头
msg['from'] = "378699049@qq.com"
msg['to'] = "beijinglixun@gmail.com"
msg['Subject'] = "from python"

# 附件
with open("../report/report.html","rb") as f:
    att_file = f.read()

att = MIMEText(att_file, 'base64','utf_8')
att["Content-Type"] = 'application/octet-stream' # 声明附件的内容格式 MIME数据流格式
att["Content-Disposition"] = "attachment;filename='report.html'" # 附件描述信息 filename是附件显示的文件名
msg.attach(att)

# 连接SMTP服务器并发送
smtp = smtplib.SMTP("smtp.qq.com")
smtp.login("378699049@qq.com","ajkxtszgxqaybijd")
smtp.sendmail("378699049@qq.com",
              "beijinglixun@gmail.com",
              msg.as_string())

