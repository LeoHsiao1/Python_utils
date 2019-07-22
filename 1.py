import smtplib
from email.header import Header
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


# server = smtplib.SMTP(host="localhost", port=25)  # 连接到SMTP服务器
server = smtplib.SMTP_SSL(host="smtp.163.com", port=994, timeout=3)  # 基于SSL协议连接到SMTP服务器
server.login("will1334@163.com", "password")


msg = MIMEMultipart()
msg["From"] = Header("Python smtplib", "utf-8")     # 注明发送者
msg["To"] = Header("Mr. Van Helsing", "utf-8")      # 注明接收者
msg["Subject"] = Header("这是一封测试邮件", "utf-8")  # 写入标题
content = "Python邮件发送测试..."
msg.attach(MIMEText(content, "plain", "utf-8"))     # 写入邮件内容
# 内容类型设置为"html"，就可以发送HTML内容


# 上传附件（可照这样attach多个附件）
with open(r"D:\1\test_Python\7.jpg", "rb") as f:
    attachment = MIMEApplication(f.read())
    attachment.add_header("Content-Disposition", "attachment", filename="1.jpg")
    msg.attach(attachment)


sender = "will1334@163.com"      # 这里要填有效的邮箱地址
receiver = "will1334@163.com"    # 可以是一个序列，发送给多个邮箱地址
server.sendmail(sender, receiver, msg.as_string())
server.quit()  # 关闭连接
