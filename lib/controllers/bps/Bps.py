from flask import Blueprint;
from flask_restx import Resource;
from lib.helpers import TypeEnums;
from lib.controllers import api;
from flask import Blueprint, request, send_file;
from lib import Bps;
from json import dumps;
import os;


bps = Blueprint("bps-controller", __name__)
ns_api = api.namespace("api/v1/bps", description="Badan Pusat Statistik")
search = Bps();

def write(path: str, data: str) -> None:
    if(not os.path.exists('/'.join(path.split('/')[:-1]))):
        os.makedirs('/'.join(path.split('/')[:-1]));
        # os.makedirs(path);

    with open(path, 'w') as file:
        file.write(data);

@ns_api.route("/sosial", methods=["GET"])
class Sosial(Resource):
    @api.doc(
        params={
            "option": {
                "description": "Parameters to determine the option",
                "enum": [e.name for e in TypeEnums.Sosial_Kependudukan],
                "default": TypeEnums.Sosial_Kependudukan.GENDER.name
            },
        },
    )
    def get(self):
        option = request.values.get("option");
        url = TypeEnums.Sosial_Kependudukan[option].value;

        data: str = search.execute(url);

        write(f'data/Sosial_Kependudukan/{TypeEnums.Sosial_Kependudukan[option].name}.json',dumps(data))

        return data;

@ns_api.route("/ekonomi", methods=["GET"])
class Ekonomi(Resource):
    @api.doc(
        params={
            "option": {
                "description": "Parameters to determine the option",
                "enum": [e.name for e in TypeEnums.Ekonomi_Perdagangan],
                "default": TypeEnums.Ekonomi_Perdagangan.ENERGI.name
            },
        },
    )
    def get(self):
        option = request.values.get("option");
        url = TypeEnums.Ekonomi_Perdagangan[option].value;

        data: str = search.execute(url);

        write(f'data/Ekonomi/{TypeEnums.Ekonomi_Perdagangan[option].name}.json',dumps(data))

        return data;

@ns_api.route("/pertanian", methods=["GET"])
class Pertanian(Resource):
    @api.doc(
        params={
            "option": {
                "description": "Parameters to determine the option",
                "enum": [e.name for e in TypeEnums.Pertanian_Pertambangan],
                "default": TypeEnums.Pertanian_Pertambangan.HORTIKULTURA.name
            },
        },
    )
    def get(self):
        option = request.values.get("option");
        url = TypeEnums.Pertanian_Pertambangan[option].value;

        data: str = search.execute(url);

        write(f'data/Pertanian_Pertambangan/{TypeEnums.Pertanian_Pertambangan[option].name}.json',dumps(data))

        return data;

@ns_api.route("/test", methods=["GET"])
class Test(Resource):
    
    @api.doc(
        params={
            "option": {
                "description": 'test',
                "enum": Bps().test(),
                "default": TypeEnums.Pertanian_Pertambangan.HORTIKULTURA.name
            },
        },
    )
    def get(self):
        option = request.values.get("option");
        url = TypeEnums.Pertanian_Pertambangan[option].value;
        search = Bps();

        return search.execute(url);