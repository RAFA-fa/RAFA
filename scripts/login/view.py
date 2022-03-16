# import hashlib
#
# from flask import request
# from flask import render_template
#
# # from app import app
# from scripts.login.forms import UserForm
# from scripts.login.models import User, db
#
# session = db.session
#
#
# def setPassword(password):
#     md5 = hashlib.md5()
#     md5.update(password.encode())
#     result = str(md5.hexdigest())
#     return result
#
#
# @app.route("/register", methods=["POST", "GET"])
# def register():
#     error = "empty"
#     if request.method == "POST":
#         data = UserForm(request.form)
#         if data.validate():
#             clean_data = data.data
#             user = User(
#                 name=clean_data["name"],
#                 password=setPassword(clean_data["password"]),
#                 email=clean_data["email"]
#             )
#             session.add(user)
#             session.commit()
#             error = "success"
#         else:
#             error = data.errors
#
#     # return render_template('register.html', error=error)
#     return "hello"