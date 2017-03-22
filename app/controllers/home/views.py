# -*- coding:utf-8 -*-
from flask import render_template
from flask.ext.login import login_required

from . import home
from core.dataimpl import source_impl


@home.route('/', methods=['GET'])
#@login_required
def index():
    s = source_impl.get_all_active(True)
    return render_template('home/index.html', sources=s)