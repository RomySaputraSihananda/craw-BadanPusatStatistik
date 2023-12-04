from flask import Flask
from gevent.pywsgi import WSGIServer
from lib import sdk
from lib.controllers.bps import Ekonomi

if __name__ == "__main__":
    port = 4444;

    class App(Flask):
        def __init__(self, import_name, **kwargs):
            super().__init__(import_name)

    app = App(__name__)
    app.register_blueprint(sdk)
    application = app

    print(f"listening to http://localhost:{port} ....")
    http_server = WSGIServer(("localhost", port), application)
    http_server.serve_forever()
