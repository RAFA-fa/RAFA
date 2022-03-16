from flask import Flask, jsonify, flash
from flask import render_template, redirect, request
from utils import DataSelect
from pictures import DrawPictures
import base64
from flask_sqlalchemy import SQLAlchemy
from login import RegisterForm, LoginForm, app, User, db, session,setPassword


@app.route('/')
def rafa():
    return redirect('/login')


@app.route('/register', methods=['GET', 'POST'])
def Register():
    if request.method == 'GET':
        RetForm = RegisterForm()
        return render_template('register.html', form=RetForm)
    else:
        RetForm = RegisterForm(formdata=request.form)
        # print(RetForm.data.get('username'))
        # print(RetForm.data.get('email'))
        name_unique = len(User.query.filter(User.name == RetForm.data.get('username')).all())
        # print(name_unique)
        email_unique = len(User.query.filter(User.email == RetForm.data.get('email')).all())
        # print(email_unique)
        # passwordlable = RetForm.data.get('password') == RetForm.data.get('RepeatPassword')
        if RetForm.validate() and name_unique and email_unique:
            flash("该用户名和email均已被注册")
        elif RetForm.validate() and name_unique:
            flash("该用户名已被注册")
        elif RetForm.validate() and email_unique:
            flash("该邮箱已被注册")
        elif RetForm.validate():
            user = User(name=RetForm.data.get('username'),
                        email=RetForm.data.get('email'),
                        password=setPassword(RetForm.data.get('password')))
            session.add(user)
            session.commit()
            session.close()
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
        Information_email = User.query.filter(User.email == RetForm.data.get('username')
                                      ).all()
        # print(Information_email)
        Information_name = User.query.filter(User.name == RetForm.data.get('username')).all()
        # print(Information_name)
        Information = Information_email+Information_name
        # print(Information)
        email_label = len(Information)
        if RetForm.validate() and not email_label:
            flash("该邮箱不存在")
        elif RetForm.validate() and email_label:
            password_label = (Information[0].password == setPassword(RetForm.data.get('password')))
            if not password_label:
                flash("密码输入错误")

            else:
                temp = RetForm.data
                print("接收到数据:", temp)
                # return '''<script type="text/javascript">alert('登录完成!');</script>'''
                return redirect('/admin')
        else:
            print(RetForm.errors)
        return render_template('log_in.html', form=RetForm)





# @app.route("/", methods=["GET", "POST"])
# def register():
#     # error = "empty"
#     form = UserForm(request.form)
#     if request.method == "POST":
#         if form.validate_on_submit():
#             username = request.form.get('user_name')
#             password = request.form.get('password')
#             print(password)
#             # user = User(name=username,
#             #             password="123",
#             #             )
#             # print(user)
#             # print("验证成功")
#             # session.add(user)
#             # session.commit()
#             # session.close()
#             user = User(name=username,
#                         password=password,
#                         )
#             # print(ret)
#             session.add(user)
#             session.commit()
#             session.close()
#
#             return redirect('/admin')
#         else:
#             print("验证失败")


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
    # db.drop_all()
    # db.create_all(app=app)
    # ret = Article(title='322', author='33', content='222')
    # user = User(name="12345",
    #             email="904311450@qq.com",
    #             password="123",
    #             )
    # # print(ret)
    # session.add(user)
    # session.commit()
    # session.close()
    app.run()

    # print(User.query.filter(User.name == '12345').all())
    # label = len(User.query.filter(User.name == '123').all())
    # print(label)
    # print(User.query.filter().all()[1])
