#!/usr/bin/env python3
"""
E2e test for the app module
"""

import requests


def register_user(email: str, password: str) -> None:
    """
    Register a user
    """
    response = requests.post(
        'http://localhost:5000/users',
        data={'email': email, 'password': password})
    assert response.status_code == 200


def log_in_wrong_password(email: str, password: str) -> None:
    """
    Login a user with wrong password
    """
    response = requests.post(
        'http://localhost:5000/sessions',
        data={'email': email, 'password': 'wrongpassword'})
    assert response.status_code == 401


def log_in(email: str, password: str) -> str:
    """Login a user
    """
    response = requests.post(
        'http://localhost:5000/sessions',
        data={'email': email, 'password': password})
    assert response.status_code == 200
    return response.cookies.get('session_id')


def log_out(session_id: str) -> None:
    """Logout a user
    """
    response = requests.delete(
        'http://localhost:5000/sessions', cookies={'session_id': session_id})
    assert response.status_code == 200


def profile_unlogged() -> None:
    """Profile of a user
    """
    response = requests.get('http://localhost:5000/profile')
    assert response.status_code == 403


def profile_logged(session_id: str) -> None:
    """Profile of a user
    """
    response = requests.get(
        'http://localhost:5000/profile', cookies={'session_id': session_id})
    assert response.status_code == 200
    # assert response.json().get('message') == 'logged in'


def reset_password_token(email: str) -> str:
    """Reset password token
    """
    response = requests.post(
        'http://localhost:5000/reset_password', data={'email': email})
    assert response.status_code == 200
    return response.json().get('reset_token')


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """Update password
    """
    response = requests.put(
        'http://localhost:5000/reset_password',
        data={'email': email, 'reset_token': reset_token,
              'new_password': new_password})
    assert response.status_code == 200
    assert response.json().get('message') == 'Password updated'


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
