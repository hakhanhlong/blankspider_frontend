# -*- coding:utf-8 -*-
from flask import render_template, flash
from flask_login import login_required

from . import home
from core.dataimpl import source_impl


@home.route('/', methods=['GET'])
#@login_required
def index():
    try:
        s = source_impl.get_all_active(True)
        return render_template('home/index.html', sources=s)
    except Exception as ex:
        flash('ERROR:' + ex.message, 'danger')

    return render_template('home/index.html')