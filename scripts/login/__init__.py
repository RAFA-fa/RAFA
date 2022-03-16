import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect as CsrfProtece
from datetime import timedelta

#
# app = Flask(__name__)
#
# BaseDir = os.path.join(
#     os.path.dirname(
#         os.path.abspath(__file__)
#     )
# ).split("\\",1)[1]
#
# db_path = "sqlit:////"+BaseDir.replace("\\","/")
# # app = Flask(__name__)
# # 设置静态文件缓存过期时间
# app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)
# # 保护后端操作
# app.config['SECRET_KEY'] = 'ASDNM'
#
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:940530@127.0.0.1/students'#mysql协议，mysql用户名，地址，数据库名
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =True #开启消耗性能
# CsrfProtece(app)
# #SQLAlchemy和app绑定起来
# db = SQLAlchemy(app)