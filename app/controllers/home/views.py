# -*- coding:utf-8 -*-
from flask import render_template
from flask.ext.login import login_required

from . import home


@home.route('/', methods=['GET'])
#@login_required
def index():
    return render_template('home/index.html')