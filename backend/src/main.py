# coding=utf-8

from flask import Flask, jsonify, request
from database import Database
from vehicle_registration_service import register_vehicle

app = Flask(__name__)
database = Database()

@app.route('/vehicles')
def get_vehicles():
  # TODO
  return jsonify({})

@app.route('/vehicles', methods=['POST'])
def create_vehicle():
  # TODO
  return jsonify({})

@app.route('/vehicles/<id>')
def get_vehicle(id):
  # TODO
  return jsonify({})

@app.route('/vehicles/<id>', methods=['PATCH'])
def update_vehicle(id):
  # TODO
  return jsonify({})

@app.route('/vehicles/<id>', methods=['DELETE'])
def delete_vehicle(id):
  # TODO
  return jsonify({})
