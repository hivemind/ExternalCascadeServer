"""
======================
MicroCascade Server
----------------------
This server is intended to be used paired with the "External Source" functionality of the app "3+ Levels Cascade" on
the Atlassian Marketplace

Link
https://marketplace.atlassian.com/apps/1235004/3-levels-cascade-fields

Deploy the server, manage the options and then use the endpoint
<host>/options/field/customfield_xxxxx

Where xxxxx is your field ID.

If you need any help with this, get in touch in our portal
https://hivemind-developers.atlassian.net/servicedesk/customer/portals
"""

from flask import request, jsonify
from app.extensions import db
from app.factory import app_factory
from app.models.options import CustomfieldOptions
from config import DEBUG, PORT

app = app_factory()


def error(message):
    """
    Returns a dictionary with an error message.

    Args:
        message (str): The error message to be returned.

    Returns:
        dict: A dictionary containing the error message.
    """
    return {"message": "Error", "error": message}


@app.route("/createModel")
def create_model():
    """
    Creates the database model by running `db.create_all()`.

    Returns:
        tuple: A success message and an HTTP status code 200.
    """
    db.create_all()
    return "Model created successfully", 200


# CREATE
@app.post('/options')
def create_item():
    """
    Creates a new item in the `CustomfieldOptions` table.

    Expects:
        JSON payload containing the attributes of the new item.

    Returns:
        tuple: A JSON representation of the created item and an HTTP status code 201,
        or an error message and an HTTP status code 400 if an exception occurs.
    """
    try:
        data = request.json
        print(data)
        new_item = CustomfieldOptions(**data)
        return jsonify(new_item.to_dict()), 201
    except Exception as e:
        return error(str(e)), 400


# GET all
@app.route('/options', methods=['GET'])
def get_items():
    """
    Retrieves all items from the `CustomfieldOptions` table.

    Returns:
        tuple: A JSON list of all items and an HTTP status code 200,
        or an error message and an HTTP status code 400 if an exception occurs.
    """
    try:
        items = CustomfieldOptions.query.all()
        return jsonify([item.to_dict() for item in items]), 200
    except Exception as e:
        return error(str(e)), 400


# GET by field ID
@app.route('/options/field/<fieldId>', methods=['GET'])
def get_items_by_field(fieldId):
    """
    Retrieves all items from the `CustomfieldOptions` table filtered by `field_id`.

    Args:
        fieldId (str): The field ID to filter the items by.

    Returns:
        tuple: A JSON list of items with the specified `field_id` and an HTTP status code 200,
        or an error message and an HTTP status code 400 if an exception occurs.
    """
    try:
        items = CustomfieldOptions.query.filter_by(field_id=fieldId).all()
        return jsonify([item.to_dict() for item in items]), 200
    except Exception as e:
        return error(str(e)), 400


# GET by ID
@app.route('/options/<id>', methods=['GET'])
def get_item(id):
    """
    Retrieves a single item from the `CustomfieldOptions` table by its ID.

    Args:
        id (str): The ID of the item to retrieve.

    Returns:
        tuple: A JSON representation of the item and an HTTP status code 200,
        or an error message and an HTTP status code 400 if an exception occurs.
    """
    try:
        item = CustomfieldOptions.query.filter_by(id=str(id)).first()
        return jsonify(item.to_dict()), 200
    except Exception as e:
        return error(str(e)), 400


# UPDATE
@app.route('/options/<id>', methods=['PUT'])
def update_item(id):
    """
    Updates an existing item in the `CustomfieldOptions` table by its ID.

    Args:
        id (str): The ID of the item to update.

    Expects:
        JSON payload containing the updated attributes of the item.

    Returns:
        tuple: A JSON representation of the updated item and an HTTP status code 200,
        or an error message and an HTTP status code 400 if an exception occurs.
    """
    try:
        data = request.get_json()
        item = CustomfieldOptions.query.filter_by(id=str(id)).first().update(**data)
        return jsonify(item.to_dict()), 200
    except Exception as e:
        return error(str(e)), 400


# DELETE
@app.delete('/options/<id>')
def delete_item(id):
    """
    Deletes an item from the `CustomfieldOptions` table by its ID.

    Args:
        id (str): The ID of the item to delete.

    Returns:
        tuple: An empty response with HTTP status code 204 if successful,
        or an error message and an HTTP status code 400 if an exception occurs.
    """
    try:
        CustomfieldOptions.query.filter_by(id=str(id)).first().delete()
        return '', 204
    except Exception as e:
        return error(str(e)), 400


if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)
