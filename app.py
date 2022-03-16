from flask import Flask, jsonify
from flask import render_template, redirect, request
from jieba.analyse import extract_tags
import string
from utils import DataSelect
from pictures import DrawPictures
import matplotlib.pyplot as plt
import base64
from flask_cors import CORS
from R2picture import tab_picture
from datetime import timedelta

import hashlib
from flask_wtf.csrf import CSRFProtect as CsrfProtece
# from scripts.login.forms import UserForm
# from scripts.login.models import User,Article
from flask_sqlalchemy import SQLAlchemy
# from scripts.login import db
# from scripts.login import app

app = Flask(__name__)

# 设置静态文件缓存过期时间
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)
# 保护后端操作
app.config['SECRET_KEY'] = 'ASDNM'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:940530@127.0.0.1/students'#mysql协议，mysql用户名，地址，数据库名
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =True #开启消耗性能
CsrfProtece(app)
#SQLAlchemy和app绑定起来
db = SQLAlchemy(app)
session = db.session


class Role(db.Model):
    "角色表"
    __tablename__ = 'role'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))


class User(db.Model):
    # __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    # email = db.Column(db.String(32))
    password = db.Column(db.String(32))
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))

    def __repr__(self):
        return "<User( name='%s', password='%s')>" % (self.name, self.password)



class Article(db.Model):
    __tablename__ = 'article'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    author = db.Column(db.String(50))
    content = db.Column(db.String(12))

    def __repr__(self):
        return "<Article(title='%s', author='%s', content='%s')>" % (self.title, self.author, self.content)

from flask_wtf import FlaskForm

import wtforms
from wtforms import validators


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



# app.config['JSON_AS_ASCII'] = False  # 解决flask接口中文数据编码问题
# # 设置可跨域范围
# CORS(app, supports_credentials=True)

def setPassword(password):
    md5 = hashlib.md5()
    md5.update(password.encode())
    result = str(md5.hexdigest())
    return result


@app.route("/", methods=["GET", "POST"])
def register():
    # error = "empty"
    form = UserForm(request.form)
    if request.method == "POST":
        if form.validate_on_submit():
            username = request.form.get('user_name')
            password = request.form.get('password')
            print(password)
            # user = User(name=username,
            #             password="123",
            #             )
            # print(user)
            # print("验证成功")
            # session.add(user)
            # session.commit()
            # session.close()
            user = User(name=username,
                        password=password,
                        )
            # print(ret)
            session.add(user)
            session.commit()
            session.close()

            return redirect('/admin')
        else:
            print("验证失败")

        # form = UserForm()
        # a = form.name
        # print(a)

        # form = UserForm(request.form)

        # print(data.validate())

        # if form.validate_on_submit():
        # #     clean_data = data.data
        # #     user = User(
        # #         name=clean_data["name"],
        # #         password=setPassword(clean_data["password"]),
        # #         # email=clean_data["email"]
        # #     )
        # #     session.add(user)
        # #     session.commit()
        # #     error = "success"

        # else:
        #     print("验证失败")
        # else:
        #     error = data.errors

    # return render_template('register.html', error=error)
    return render_template('login.html', form=form)


# 展示Flask如何读取服务器本地图片, 并返回图片流给前端显示的例子
def return_img_stream(img_local_path):
    """
    工具函数:获取本地图片流
    :param img_local_path:文件单张图片的本地绝对路径
    :return: 图片流
    """
    with open(img_local_path, 'rb') as img_f:
        img_stream = img_f.read()
        img_stream = base64.b64encode(img_stream).decode()

    return img_stream


@app.route("/admin")
def hello_world():
    img_path = 'D:/Software/Pycharm/Pycharm2019/Project3/RAFA/static/img/test.png'
    plot_url = return_img_stream(img_path)
    img_path1 = 'D:/Software/Pycharm/Pycharm2019/Project3/RAFA/static/img/lime.png'
    plot_url1 = return_img_stream(img_path1)
    # 函数是flask函数，它从模版文件夹templates中呈现给定的模板上下文。
    return render_template('index.html', plot_url=plot_url, plot_url1=plot_url1)
    # return render_template('index.html')


dtsl = DataSelect()


@app.route("/time")
def get_time():
    return dtsl.get_time()


@app.route("/demo")
def get_demographic_data():
    res = dtsl.get_demographic_data()
    return jsonify({"Age": res[3], "Gender": res[4], "Height": res[6], "Weight": res[7], "INICUDATETIME": res[21]})


@app.route("/lab")
def get_lab_data():
    res = dtsl.get_lab_data()
    return jsonify({"Charttime": res[3], "CLUCOSE": res[4], "PO2": res[5], "PAO2": res[6], "PCO2": res[8],
                    "PH": res[9], "BASE_EXCESS": res[10], "TOTALCO2": res[11], "LACTATE": res[12]})


# 实例化一个对象
p_0 = 0.67
drawpictures = DrawPictures()


@app.route("/l1")
def get_vital_chart():
    c = drawpictures.vital_line()
    return c.dump_options_with_quotes()


# 脓毒症危险指数变化图 l2
@app.route("/l2")
def get_line_chart():
    p0 = format(p_0, '0.4f')
    c = drawpictures.creat_pressure_chart(p0)
    return c.dump_options_with_quotes()


@app.route("/r1")
def get_pressure_chart3():
    c = drawpictures.Gender_Bar()
    return c.dump_options_with_quotes()


@app.route("/r2")
def get_pressure_chart4():
    p0 = format(p_0, '0.4f')
    c = drawpictures.creat_pressure_chart(p0)
    return c.dump_options_with_quotes()


if __name__ == '__main__':
    # db.create_all()
    # ret = Article(title='322', author='33', content='222')
    # user = User(name="123",
    #             password="123",
    #             )
    # # print(ret)
    # session.add(user)
    # session.commit()
    # session.close()
    app.run()

# from flask_cors import CORS

# app.config['JSON_AS_ASCII'] = False  # 解决flask接口中文数据编码问题
#
# # 设置可跨域范围
# CORS(app, supports_credentials=True)
#
#
#
# if __name__ == '__main__':
#     # app.run(host, port, debug, options)
#     # 默认值：host="127.0.0.1", port=5000, debug=False
#     app.run(host="127.0.0.1", port=5010)
