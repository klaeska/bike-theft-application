from api.middlewares import login_required
from flask import Flask, json, g, request
from app.bikeApp.service import Service as BikeApp
from app.bikeApp.schema import BikeInfoSchema
from flask_cors import CORS
import logging

app = Flask(__name__)
CORS(app)


@app.route("/bikes", methods=["GET"])
def index():
    return json_response(BikeApp(g.user).find_all_bikes())


@app.route("/bike", methods=["POST"])
@login_required
def create(): 
    bike_info = BikeInfoSchema().load(json.loads(request.data))

    bike = BikeApp(g.user).create_bike_for(bike_info)
    return json_response(bike)


@app.route("/bike/<int:bike_id>", methods=["GET"])
def show(bike_id):
    bike = Bike(g.user).find_bike(bike_id)

    if bike:
        return json_response(bike)
    else:
        return json_response({'error': 'bike not found'}, 404)


@app.route("/bike/<int:bike_id>", methods=["PUT"])
@login_required
def update(bike_id):
    bike_info = BikeInfoSchema().load(json.loads(request.data))
    
    bike_service = BikeApp(g.user)
    if bike_service.update_bike_with(bike_id, bike_info):
        return json_response(bike_info.data)
    else:
        return json_response({'error': 'bike not found'}, 404)


@app.route("/bike/<int:bike_id>", methods=["DELETE"])
@login_required
def delete(bike_id):
    bike_service = BikeApp(g.user)
    if bike_service.delete_bike_for(bike_id):
        return json_response({})
    else:
        return json_response({'error': 'bike not found'}, 404)


def json_response(payload, status=200):
    return (json.dumps(payload), status, {'content-type': 'application/json'})