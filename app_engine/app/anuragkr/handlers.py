# -*- coding: utf-8 -*-

from ..anuragkr import anuragkr
from flask import render_template

@anuragkr.route('/')
def anuragkr():
    return render_template("base.html")
