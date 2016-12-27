# -*- coding=utf-8 -*-
"""
email 类
"""
from mailConfig import template_config

class EmailTemple(object):
    """
    Email 模板类
    """
    def __init__(self, template_name='defaultTemplateEmail',file_suffixes='.html'):
        self.file_suffixes = file_suffixes
        self.template_name = template_name

    def get_temple(self):
        """
        获取邮件模板
        :return: 邮件模板
        """
        return self._get_temple_on_file()

    def _get_temple_on_file(self):
        """
        读取邮件模板
        :return: 邮件模板
        """
        template = ''
        with open('template/' + self.template_name + self.file_suffixes, 'r', encoding='utf-8') as template_file:
            for line in template_file:
                template = template + line
        return template

class Iemail(object):
    """
    Email 类
    """
    def __init__(self, email_type='text',
                 template_name='defaultTemplateEmail',
                 file_suffixes='.html'):
        self.email_type = email_type
        self.file_suffixes = file_suffixes
        self.template_name = template_name

    def set_mail(self, **args):
        """
        设置邮件内容
        :param args: 邮件模板参数
        :return: 邮件内容
        """
        if self.email_type == 'text':
            if 'message' in args:
                self.content = args['message']
            else:
                raise RuntimeError('ErrorMessage: 请输入邮件内容！！')
        else:
            if self.template_name in template_config:
                # 获取模板内容
                emailTemple = EmailTemple(template_name=self.template_name,
                                          file_suffixes=self.file_suffixes).get_temple()
                # 检查参数
                for need_arg in template_config[self.template_name]:
                   if need_arg not in args: raise RuntimeError('ErrorMessage: 缺少参数 ' + need_arg)
                   self.content = emailTemple.format(**args)

    def get_mail(self):
        """
        获取邮件内容
        :return: 邮件内容
        """
        if not self.content:
            raise RuntimeError('ErrorMessage: 请先初始化 Mail!')
        return self.content