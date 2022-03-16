from app import db


# 创建数据库模型类

# class Role(db.Model):
#     "角色表"
#     __tablename__ = 'role'
#
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(32))
#
#
# class User(db.Model):
#     # __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(32))
#     # email = db.Column(db.String(32))
#     password = db.Column(db.String(32))
#     role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
#
#     def __repr__(self):
#         return "<User( name='%s', password='%s')>" % (self.name, self.password)
#
#     # def __repr__(self):
#     #     return self.name
#
#
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

