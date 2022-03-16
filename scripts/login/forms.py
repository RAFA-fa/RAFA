from flask_wtf import FlaskForm

import wtforms
from wtforms import validators
from scripts.login.models import User


class EmailValider:
    def __init__(self, message):
        self.message = message

    def __call__(self, form, field):
        data = field.data
        user = User.query.filter_by(email=data).all()
        if not user:
            return None

        raise validators.ValidationError(self.message)


class UserForm(FlaskForm):
    # ID = wtforms.StringField("ID", validators=[validators.DataRequired(),
    #
    #             # validators.Regexp(regex=r"[0-9a-zA-Z]{2,8}", message="用户名必须是数字字母下划线")
    #             ])

    user_name = wtforms.StringField("用户名", validators=[validators.DataRequired(),
        validators.length(min=2, max=8, message="用户名必须大于2位小于8位"),
        # validators.Regexp(regex=r"[0-9a-zA-Z]{2,8}", message="用户名必须是数字字母下划线")
    ])
    # email = wtforms.StringField("用户邮箱", validators=[
    #     validators.Regexp(regex=r"\w+@\w+\.\w+", message="邮箱格式错误"),
    #     EmailValider(message="邮箱重复")
    # ])
    password = wtforms.StringField("密码", validators=[validators.DataRequired(),
        validators.length(min=2, max=8, message="密码必须大于2位小于8位")
    ])
    submit = wtforms.SubmitField(label='提交')