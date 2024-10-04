import json
import pytest_html

def test_index(app, client):
    del app
    res = client.get('/')
    assert res.status_code == 200

def test_html(app,client):
    del app
    response = client.get('/')
    assert b"Welcome to the Geographic Data Directory" in response.data
    assert b"Get JSON Data" in response.data
