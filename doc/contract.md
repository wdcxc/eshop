---
title: 公约
---

[toc]

---

# project 

项目名：eshop

更新数据库需要执行下面命令

```shell
manage.py makemigrations
manage.py migrate
```

---

# app

|名称|对应模块|
|-|-|
|admin|平台管理者|
|customer|顾客|
|seller|商家|

---

# js

## vue

### 资源

[awesome-vue](https://github.com/vuejs/awesome-vue#routing)

---

# 返回格式

## ajax 

### json

{code:num,msg:string,data:object}

---

# 返回码

## Django

|码值|位置|说明|
|-|-|
|200|*|返回成功|
|401|customer:doLogin|验证码错误|
|(已弃用)402|customer.doLogin|账号或密码错误|
|403|customer.register|用户名格式错误|
|404|customer.register|密码格式错误|
|405|customer.register|手机格式错误|
|406|customer.register|邮箱格式错误|
|407|customer.register|用户名已存在|
|408|customer.register|手机已存在|
|409|customer.register|邮箱已存在|
|410|customer.login|账号或密码错误|
|411|customer.captchaValify|验证码错误|
|411|customer.doRegister|验证码错误|
