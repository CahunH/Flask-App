from flask import Blueprint, jsonify
main = Blueprint('main', _name_)
@main.route('/')
def index():
  return jsonify({'message': 'Hello, World!'})
  
