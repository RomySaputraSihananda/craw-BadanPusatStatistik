from flask import Blueprint;
from flask_restx import Resource;
from lib.helpers import TypeEnums;
from lib.controllers import api;
from flask import Blueprint, request, send_file
from lib import Bps;

bps = Blueprint("bps-controller", __name__)
ns_api = api.namespace("api/v1/bps", description="Badan Pusat Statistik")

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
        search = Bps();

        return search.execute(url);

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
        search = Bps();

        return search.execute(url);

@ns_api.route("/pertanian", methods=["GET"])
class Pertanian(Resource):
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
        search = Bps();

        return search.execute(url);