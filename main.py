import argparse

# from flask import Flask
# from gevent.pywsgi import WSGIServer
from json import dumps

# from lib import sdk
from lib.helpers import logging
from lib.controllers.bps import Bps
from lib.helpers.TypeEnums import Sosial_Kependudukan, Ekonomi_Perdagangan, Pertanian_Pertambangan

import os 

def loop_write(main: str, options: any, *args) -> None:
    for topic in options:
        data: str = dumps(bps.execute(topic.value))

        path_output: str = f'data/{main}/{topic.name}.json'

        if(not os.path_output.exists('/'.join(path_output.split('/')[:-1]))):
            os.makedirs('/'.join(path_output.split('/')[:-1]))

        with open(path_output, 'w') as file:
            file.write(data)

if __name__ == "__main__":
    argp = argparse.ArgumentParser()
    argp.add_argument("--topic", '-t', type=str)
    argp.add_argument("--server", '-s', type=bool)
    argp.add_argument("--port", '-p', type=int, default=4444)
    args = argp.parse_args()

    # if(args.server):
    #     class App(Flask):
    #         def __init__(self, import_name, **kwargs):
    #             super().__init__(import_name)

        # app = App(__name__)
        # app.register_blueprint(sdk)
        # application = app


        # logging.info(f"listening  -> http://localhost:{args.port} ....")
        # logging.info(f"swagger-ui -> http://localhost:{args.port}/docs ....")
        # http_server = WSGIServer(("localhost", args.port), application)
        # http_server.serve_forever()

    if(args.topic):
        from lib.services import Bps
    
        bps: Bps = Bps()

        match(args.topic.upper()):
            case 'SOSIAL':
                loop_write('Sosial', Sosial_Kependudukan)
            case 'EKONOMI':
                loop_write('Ekonomi', Ekonomi_Perdagangan)
            case 'PERTANIAN':
                loop_write('Pertanian', Pertanian_Pertambangan)

    
    logging.info("admitted smoothly")




