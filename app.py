import os
import boto3
from flask import Flask, jsonify, make_response, request
import uuid

app = Flask(__name__)

# Create a DynamoDB client
dynamodb_client = boto3.client('dynamodb')

# Get the table name from environment variable
USERS_TABLE = os.environ['USERS_TABLE']

@app.route('/users/<string:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    """
    Get a user by user_id
    Args:
        user_id (str): user_id to get
        Returns:
        dict: User details
    """
    # Get the user from DynamoDB
    result = dynamodb_client.get_item(
        TableName=USERS_TABLE, Key={'userId': {'S': user_id}}
    )

    item = result.get('Item')
    if not item:
        return jsonify({'error': 'Could not find user with provided "userId"'}), 404

    return jsonify(
        {'userId': item.get('userId').get('S'), 'name': item.get('name').get('S')}
    )


@app.route('/users', methods=['POST'])
def create_user():
    """
    Create a new user
    Returns:
    dict: User details
    """

    name = request.json.get('name')
    if not name:
        return jsonify({'error': 'Please provide "name"'}), 400

    user_id = uuid.uuid4().hex

    # Add the user to DynamoDB
    dynamodb_client.put_item(
        TableName=USERS_TABLE, Item={'userId': {'S': user_id}, 'name': {'S': name}}
    )

    return jsonify({'userId': user_id, 'name': name})


@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)
