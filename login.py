from flask import Flask, render_template, request, redirect, flash
from wtforms import Form, validators, widgets
from wtforms.fields import simple

from flask_wtf.csrf import CSRFProtect as CsrfProtece
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
import hashlib
# 设置静态文件缓存过期时间
app = Flask(__name__, template_folder="templates")
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)
# 保护后端操作
app.config['SECRET_KEY'] = 'ASDNM'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:940530@127.0.0.1/students'  # mysql协议，mysql用户名，地址，数据库名
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True  # 开启消耗性能
CsrfProtece(app)
# SQLAlchemy和app绑定起来
db = SQLAlchemy(app)
session = db.session


# class Role(db.Model):
#     "角色表"
#     __tablename__ = 'role'
#
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(32))


class User(db.Model):
    # __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    email = db.Column(db.String(32), unique=True)
    password = db.Column(db.String(32))

    # repassword = db.Column(db.String(32))
    # role_id = db.Column(db.Integer, db.ForeignKey('role.id'))

    def __repr__(self):
        return "<User( name='%s', email = '%s',password='%s')>" \
               % (self.name, self.email, self.password)


# class Article(db.Model):
#     __tablename__ = 'article'
#
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(50))
#     author = db.Column(db.String(50))
#     content = db.Column(db.String(12))
#
#     def __repr__(self):
#         return "<Article(title='%s', author='%s', content='%s')>" % (self.title, self.author, self.content)


class RegisterForm(Form):
    username = simple.StringField(
        # label='注册用户：',
        validators=[
            validators.DataRequired(message='用户名不能为空'),
            validators.Length(min=6, max=18, message='用户名长度必须大于%(min)d且小于%(max)d')
        ],
        widget=widgets.TextInput(),
        render_kw={'class': 'form-control',
                   "placeholder": "输入注册用户名"}
    )
    email = simple.StringField(
        # label='用户邮箱：',
        validators=[validators.DataRequired(message='邮箱不能为空'), validators.Email(message="邮箱格式输入有误")],
        render_kw={'class': 'form-control',
                   "placeholder": "输入Email邮箱"}
    )
    password = simple.PasswordField(
        # label='用户密码：',
        validators=[
            validators.DataRequired(message='密码不能为空'),
            validators.Length(min=5, message='用户名长度必须大于%(min)d'),
            validators.Regexp(regex="[0-9a-zA-Z]{5,}", message='密码不允许使用特殊字符')
        ],
        widget=widgets.PasswordInput(),
        render_kw={'class': 'form-control',
                   "placeholder": "输入用户密码"}
    )
    RepeatPassword = simple.PasswordField(
        # label='重复密码：',
        validators=[
            validators.DataRequired(message='密码不能为空'),
            validators.Length(min=5, message='密码长度必须大于%(min)d'),
            validators.Regexp(regex="[0-9a-zA-Z]{5,}", message='密码不允许使用特殊字符'),
            validators.EqualTo("password", message="两次密码输入必须一致")
        ],
        widget=widgets.PasswordInput(),
        render_kw={'class': 'form-control',
                   "placeholder": "再次输入密码"}
    )
    submit = simple.SubmitField(
        label="点击注册",
        render_kw={"class": "btn btn-success btn-lg"}
    )


class LoginForm(Form):
    username = simple.StringField(
        validators=[
            validators.DataRequired(message=''),
            validators.Length(min=4, max=18, message=''),
            validators.Regexp(regex="[0-9a-zA-Z]{4,15}", message='')
        ],
        widget=widgets.TextInput(),
        render_kw={"class": "form-control",
                   "placeholder": "请输入用户名或电子邮件"}
    )
    password = simple.PasswordField(
        validators=[
            validators.DataRequired(message=''),
            validators.Length(min=5, max=15, message=''),
            validators.Regexp(regex="[0-9a-zA-Z]{5,15}", message='')
        ],
        widget=widgets.PasswordInput(),
        render_kw={"class": "form-control",
                   "placeholder": "请输入密码"}
    )

def setPassword(password):
    md5 = hashlib.md5()
    md5.update(password.encode())
    result = str(md5.hexdigest())
    return result


if __name__ == '__main__':
    app.run()
