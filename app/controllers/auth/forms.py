# -*- coding:utf-8 -*-


from wtforms import StringField, PasswordField, BooleanField, Form
from wtforms.validators import DataRequired


class LoginForm(Form):
    username = StringField(u'Tên đăng nhập', validators=[DataRequired()])
    password = PasswordField(u'Mật khẩu', validators=[DataRequired()])
    remember = BooleanField(u'Ghi nhớ mật khẩu')

