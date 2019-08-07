#!/usr/bin/python
# -*- coding:utf-8 -*-

import requests

#登录案例

def login(s,admin,pwd):
    s = requests.session()
    url = "http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html"
    headers ={
        "Content-Type": "application/x-www-form-urlencoded"
    }
    body = {
        "account":admin,
        "password":pwd,
        "referer":"http://127.0.0.1/zentao/my/",
        "keepLogin[]": "on"
    }

    r = s.post(url,headers=headers,data=body,verify=False)
    # print(r.content.decode('utf-8'))
    return r.content.decode('utf-8')

def is_login_sucess(loginRes):
        '''
        判断是否登录成功
        :param login:登录函数返回的内容
        :return: Ture or False
        '''
        if "登录失败" in loginRes:
            print("登录失败")
            return False
        elif "parent.location=" in loginRes:
            print("登录成功")
            return True
        else:
            print("出现异常，登录失败")
            return False

if __name__ == '__main__':
    s = requests.session()
    loginRes = login(s,'admin','e10adc3949ba59abbe56e057f20f883e')
    result = is_login_sucess(loginRes)
    print(result)





















