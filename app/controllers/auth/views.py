# -*- coding:utf-8 -*-
from flask import render_template, redirect, url_for, request, flash, g

from core.dataimpl.account_impl import get_by_username
from . import auth

from .forms import LoginForm
from flask_login import login_user, current_user
from core.dataimpl import account_impl


from app import login_manager


@login_manager.user_loader
def load_user(username):
    return get_by_username(username)

@auth.before_request
def get_current_user():
    if current_user.is_authenticated:
        g.user = current_user


@auth.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        form = LoginForm(request.form)
        '''if form.validate():
            try:
                account = get_by_username(username=form.username.data)
                if account is not None and account.verify_password(form.password.data):
                    login_user(account, form.remember.data)
                    return redirect(url_for('home.index'))


            except Exception as ex:
                flash('#ERROR LOGIN:' + ex.message)'''
    else:
        form = LoginForm()
        return render_template('auth/login.html', form=form)

