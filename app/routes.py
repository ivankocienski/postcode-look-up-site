from . import controllers

def define(app):
    app.route('/', methods=['GET'])(controllers.respond_root)
    app.route('/search', methods=['GET'])(controllers.respond_search)