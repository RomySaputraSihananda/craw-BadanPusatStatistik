from flask import Blueprint
from flask_restx import Api

sdk = Blueprint("sdk", __name__)
api = Api(
    app=sdk,
    version="v1.0.0",
    title="Craw & Scrap Badan Pusat Statistik",
    description="API for get Data from Badan Pusat Statistik",
    doc='/docs'
)