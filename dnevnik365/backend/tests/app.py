from dnevnik365.backend.api.app import app

from fastapi.testclient import TestClient
from httpx import Response
import pytest


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)
