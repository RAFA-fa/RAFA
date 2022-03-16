from flask import Flask, render_template, request, redirect
from wtforms import Form, validators, widgets
from wtforms.fields import simple

app = Flask(__name__, template_folder="templates")


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
            validators.EqualTo("password", message="两次密码输入必须一致,龟孙")
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


@app.route('/register', methods=['GET', 'POST'])
def Register():
    if request.method == 'GET':
        RetForm = RegisterForm()
        return render_template('register.html', form=RetForm)
    else:
        RetForm = RegisterForm(formdata=request.form)
        if RetForm.validate():
            print('接收到数据：', RetForm.data)
            # return '''<script>alert('您的注册请求已提交!');</script>'''
            return redirect('/login')
        else:
            print(RetForm.errors)
        return render_template('register.html', form=RetForm)


@app.route("/login", methods=['GET', 'POST'])
def Login():
    if request.method == 'GET':
        RetForm = LoginForm()
        return render_template('log_in.html', form=RetForm)
    else:
        RetForm = LoginForm(formdata=request.form)
        if RetForm.validate():
            temp = RetForm.data
            print("接收到数据:", temp)
            # return '''<script type="text/javascript">alert('登录完成!');</script>'''
            return redirect('/register')
        return render_template('log_in.html', form=RetForm)


if __name__ == '__main__':
    app.run()
