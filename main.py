import argparse;

from flask import Flask;
from gevent.pywsgi import WSGIServer;
from json import dumps;

from lib import sdk;
from lib.services import Bps;
from lib.controllers.bps import Ekonomi;
from lib.helpers.TypeEnums import Ekonomi_Perdagangan;

if __name__ == "__main__":
    argp = argparse.ArgumentParser();
    argp.add_argument("--server", type=bool);
    args = argp.parse_args();

    if(args.server):
        port = 4444;
        class App(Flask):
            def __init__(self, import_name, **kwargs):
                super().__init__(import_name);

        app = App(__name__);
        app.register_blueprint(sdk);
        application = app;

        print(f"listening to http://localhost:{port} ....");
        http_server = WSGIServer(("localhost", port), application);
        http_server.serve_forever();

    bps: Bps = Bps();

    data = dumps(bps.execute(Ekonomi_Perdagangan.ENERGI.value));

    with open('data_test.json', 'w') as file:
        file.write(data);

