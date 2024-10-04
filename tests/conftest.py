import pytest
from app import app as flask_app
from bs4 import BeautifulSoup

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def client1():
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as client:
        yield client