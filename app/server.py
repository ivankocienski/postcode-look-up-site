from flask import Flask

import app.config as config

app = Flask(
    config.name(), 
    static_url_path=config.work_dir,
    static_folder=config.work_dir + '/public',
    template_folder=config.work_dir + '/app/views'
)

app.env = config.env()

def run():
    app.run(config.host(), port=config.port())
