from dnevnik365.backend.api.app import app

from fastapi.testclient import TestClient
import pytest


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)
