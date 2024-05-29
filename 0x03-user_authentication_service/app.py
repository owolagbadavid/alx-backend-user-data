#!/usr/bin/env python3
"""
Flask app
"""
from flask import Flask, jsonify, request, abort, make_response
from auth import Auth

AUTH = Auth()
app = Flask(__name__)


@app.get('/')
def bienveue():
    """Bienvenue
    """
    return jsonify({"message": "Bienvenue"})


@app.post('/users')
def users() -> str:
    """POST /users
    """
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        new_user = AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
