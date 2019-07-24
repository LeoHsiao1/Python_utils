import asyncore
import json
import smtpd
import quopri

import requests
from pop import parse


class CustomSMTPServer(smtpd.SMTPServer):
    def process_message(self, peer, mailfrom, rcpttos, data, **kwargs):	# 重载处理邮件的方法
        print("\n\n# Received email")
        print("From: ", mailfrom, peer)
        print("To: ", rcpttos)
        print("raw_data: ", data)
        print("parsed:", parse(data))

server = CustomSMTPServer(("127.0.0.1", 9000), None)  # 创建SMTP服务器
asyncore.loop()  # 异步循环运行

