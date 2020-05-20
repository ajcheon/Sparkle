"""
Configure common fixtures to be shared across all test modules.
"""
import pytest

from app import create_app
from app import db


@pytest.fixture(scope="session")
def app():
    """Configure a new instance of a Flask application for testing."""
    app = create_app()
    app.config.from_object("app.config.TestConfig")
    with app.app_context():
        db.create_all()
        yield app


@pytest.fixture
def client(app):
    """Return a test client for the app."""
    return app.test_client()