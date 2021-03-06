# -*- coding: utf-8 -*-
'''
    :file: schema.py
    :author: -Farmer
    :url: https://blog.farmer233.top
    :date: 2021/08/04 16:25:57
'''

from apiflask import Schema 
from marshmallow.fields import Email, String, Integer, Raw


class UserInSchema(Schema):
    """用于验证请求体数据

    Args:
        Schema (Schema): 验证模型
    """
    username = String(required=True)
    pwd = String(required=True)
    url = String()



class UserOutSchema(Schema):
    """用于验证响应体数据
        model的东西不是所有都能返回的，一些敏感的数据不应该返回给前端
        且有些字段是必须的、有的确可以为空
        比如：
            1. 用户的密码是不能返回的

    Args:
        Schema (Schema): 验证模型
    """
    id = Integer(strict=True)
    username = String(required=True)
    url = String()

class IconInSchema(Schema):
    icon = Raw(type="file")