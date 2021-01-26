import app.config as config
import app.db
import app.server as server
import app.routes as routes

routes.define(server.app)

server.run()