import argparse;

from flask import Flask;
from gevent.pywsgi import WSGIServer;
from json import dumps;

from lib import sdk;
from lib.controllers.bps import Bps;
from lib.helpers.TypeEnums import Ekonomi_Perdagangan, Sosial_Kependudukan;

if __name__ == "__main__":
    argp = argparse.ArgumentParser();
    argp.add_argument("--server", type=bool);
    argp.add_argument("--port", type=int, default=4444);
    args = argp.parse_args();

    if(args.server):
        class App(Flask):
            def __init__(self, import_name, **kwargs):
                super().__init__(import_name);

        app = App(__name__);
        app.register_blueprint(sdk);
        application = app;

        print(f"listening to http://localhost:{args.port} ....");
        http_server = WSGIServer(("localhost", args.port), application);
        http_server.serve_forever();

    from lib.services import Bps;
    
    bps: Bps = Bps();

    data = dumps(bps.execute(Ekonomi_Perdagangan.KOMUNIKASI.value));

    with open('data_test.json', 'w') as file:
        file.write(data);

