from . import controllers

def define(app):
    app.route('/', methods=['GET'])(controllers.respond_root)