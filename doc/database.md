---
title: eshop 数据库文档
---

[toc]

---

# 数据库配置

mysql
用户名：root 密码：root

# 数据库创建

```mysql
create database eshop;
```

# 数据表

## customer

### 用户表(customer)

|  字段名  |     类型     |            约束            |  说明  |
|----------|--------------|----------------------------|--------|
| id       |              | primary key auto_increment | 自增id |
| username | varchar(30)  | unique not null            | 用户名 |
| password | varchar(130) | not null                   | 密码   |
| mobile   | varchar(11)  | unique not null            | 手机号 |
| email    | varchar(30)  | unique not null            | 邮箱   |

### 管理员表(admin)

### 商家表(seller)