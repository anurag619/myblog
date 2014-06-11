# -*- coding: utf-8 -*-
"""
App factory module.
"""

from flask import Flask

def create_app(config):    
    app = Flask(__name__)
    app.config.from_object(config)

    # Later register blueprints here.
    # ...
    from app.anuragkr import anuragkr
    app.register_blueprint(anuragkr, url_prefix="/")
    return app
