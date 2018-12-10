import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import config

# def send_mail():
#     msg = MIMEMultipart()
#     body = MIMEText(config.body,'plain','utf-8')
#     msg.attach(body)
#
#     # 组装邮件头
#     msg['from'] = config.server
#     msg['to'] = config.receiver
#     msg['Subject'] = config.subject
#
#     # 附件
#     with open(config.report_path,"rb") as f:
#         att_file = f.read()
#
#     att = MIMEText(att_file, 'base64','utf_8')
#     att["Content-Type"] = 'application/octet-stream' # 声明附件的内容格式 MIME数据流格式
#     att["Content-Disposition"] = "attachment;filename=report.html" # 附件描述信息 filename是附件显示的文件名
#     msg.attach(att)
#
#     # 连接SMTP服务器并发送
#     smtp = smtplib.SMTP_SSL(config.server)
#     smtp.login(config.emailusername,config.emailpassword)
#     smtp.sendmail(config.sender,
#                   config.receiver,
#                   msg.as_string())


def send_mail(title, msg):
    # 发件人
    sender = config.sender
    # 收件人
    receiver = config.receiver
    # smtp服务器
    server = config.server
    # 标题
    title = title
    # 内容
    message = msg
    # 账户
    username = config.emailusername
    # 密码
    password = config.emailpassword

    msg = MIMEText(message)
    msg['Subject'] = title
    msg['From'] = sender
    msg['To'] = receiver
    # 建立连接
    # s = smtplib.SMTP(server)
    s = smtplib.SMTP_SSL(server)
    # 认证
    s.login(username, password)
    # 发送邮件
    s.sendmail(sender, receiver.split(','), msg.as_string())
    s.quit()


def send_mail_report(title):
    # 发件人
    sender = config.sender
    # 收件人
    receiver = config.receiver
    # smtp服务器
    server = config.server
    # 账户
    username = config.emailusername
    # 密码
    password = config.emailpassword
    # print config.basedir
    bodyfp = open(config.report_path, encoding='utf-8')
    body = bodyfp.read()
    msg_root = MIMEMultipart()
    msg_root["subject"] = title
    msg_root["from"] = config.sender
    msg_root["to"] = config.receiver
    msg_html = MIMEText(body, "html", 'utf-8')
    msg_root.attach(msg_html)

    att1 = MIMEText(body, 'base64', 'utf-8')
    att1['Content-Type'] = 'application/octet-stream'
    att1['Content-Disposition'] = 'attachment; filename="Report.html"'
    msg_root.attach(att1)
    # msg_root.attach()

    s = smtplib.SMTP_SSL(server)
    # 认证
    s.login(username, password)
    # 发送邮件
    s.sendmail(sender, receiver.split(','), msg_root.as_string())
    s.quit()