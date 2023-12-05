import argparse;

from flask import Flask;
from gevent.pywsgi import WSGIServer;
from json import dumps;

from lib import sdk;
from lib.controllers.bps import Bps;
from lib.helpers.TypeEnums import Sosial_Kependudukan, Ekonomi_Perdagangan, Pertanian_Pertambangan;


def loop_write(options: any) -> None:
    for option in options:
        # data = dumps(bps.execute(option.value));
        print(option.name)

if __name__ == "__main__":
    argp = argparse.ArgumentParser();
    argp.add_argument("option", type=str);
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
    
    match(args.option.upper()):
        case 'SOSIAL':
            loop_write(Sosial_Kependudukan);
        case 'EKONOMI':
            loop_write(Ekonomi_Perdagangan);
            # data = dumps(bps.execute(Ekonomi_Perdagangan.EKSPOR_IMPOR.value));
        case 'PERTANIAN':
            loop_write(Pertanian_Pertambangan);
            # data = dumps(bps.execute(Ekonomi_Perdagangan.EKSPOR_IMPOR.value));




