"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Character, Location, Episode, UserFavourite
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

@api.route('/users', methods=['GET'])
def get_all_users():
  
    response_body = {
        "message": "List of all active users:"
    }

    users = User.query.filter_by(is_active=True).all()
    users_serialized =  [user.serialize() for user in users]
    return jsonify({"Active users": users_serialized}), 200

@api.route('/characters', methods=['GET'])
def get_all_characters():
  
    response_body = {
        "message": "List of all characters:"
    }

    characters = Character.query.all()
    characters_serialized =  [character.serialize() for character in characters]
    return jsonify({"Characters": characters_serialized}), 200

@api.route('/locations', methods=['GET'])
def get_all_locations():
  
    response_body = {
        "message": "List of all locations:"
    }

    locations = Location.query.all()
    locations_serialized =  [location.serialize() for location in locations]
    return jsonify({"Locations": locations_serialized}), 200

@api.route('/episodes', methods=['GET'])
def get_all_episodes():
  
    response_body = {
        "message": "List of all episodes:"
    }

    episodes = Episode.query.all()
    episodes_serialized =  [episode.serialize() for episode in episodes]
    return jsonify({"Episodes": episodes_serialized}), 200

@api.route("/users/<int:target_user_id>/favourites", methods=['GET'])
def user_favourites(target_user_id):
    user = User.query.get(target_user_id)
    if not user:
        return jsonify("User not found"), 404

    favourites = UserFavourite.query.filter_by(user_id=target_user_id).all()
    favourites_serialized = [favourite.serialize() for favourite in favourites]
    print(favourites_serialized)
    return jsonify({"favorites": favourites_serialized}), 200

