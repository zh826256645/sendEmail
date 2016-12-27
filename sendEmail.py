# -*- coding=utf-8 -*-
"""
发送 Email
"""

from smtplib import SMTP
from email.mime.text import MIMEText

from iemail import Iemail

from mailConfig import mail_config


def send_mail(iemail, subject,to_mails, email_user=None, email_pwd=None):
    """
    发送邮件
    :param iemail: Iemail 类
    :param subject: 邮件标题
    :param to_mails: 接收邮件的用户列表
    :param email_user: 发送邮件的用户
    :param email_pwd: 发送邮件的用户密码
    :return:
    """
    # 初始化 smtp
    smtp = SMTP(mail_config['host'])
    # 初始化 mail
    mail = MIMEText(iemail.get_mail(), 'html', 'utf-8')
    # 设置 发件人
    mail['From'] = mail_config['from']
    mail['Subject'] = subject
    # 验证
    smtp.login(mail_config['from'], mail_config['pwd'])
    # 发送邮件
    smtp.sendmail(mail_config['from'], to_mails, mail.as_string())
    # 关闭
    smtp.quit()
    print('email send success')

if __name__ == '__main__':
    iemail = Iemail(email_type='html')
    iemail.set_mail(message='你好！', username='zhonghao')
    send_mail(iemail, '星期天的作业', ['826256645@qq.com'])

