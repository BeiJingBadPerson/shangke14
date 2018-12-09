import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import config

def send_mail():
    msg = MIMEMultipart()
    body = MIMEText(config.body,'plain','utf-8')
    msg.attach(body)

    # 组装邮件头
    msg['from'] = config.server
    msg['to'] = config.receiver
    msg['Subject'] = config.subject

    # 附件
    with open(config.report_path,"rb") as f:
        att_file = f.read()

    att = MIMEText(att_file, 'base64','utf_8')
    att["Content-Type"] = 'application/octet-stream' # 声明附件的内容格式 MIME数据流格式
    att["Content-Disposition"] = "attachment;filename=report.html" # 附件描述信息 filename是附件显示的文件名
    msg.attach(att)

    # 连接SMTP服务器并发送
    smtp = smtplib.SMTP(config.server)
    smtp.login(config.emailusername,config.emailpassword)
    smtp.sendmail(config.sender,
                  config.receiver,
                  msg.as_string())


