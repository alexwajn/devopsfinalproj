import pytest
import flaskcalcapp

@pytest.fixture()
def app():
    app = flaskcalcapp.app
    yield app

@pytest.fixture()
def client(app):
    return app.test_client()

