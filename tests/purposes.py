from dnevnik365.api.app import app

from fastapi.testclient import TestClient
from httpx import Response
import pytest


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)


def test_view_purposes(client: TestClient) -> None:
    response: Response = client.get('/purposes')
    assert response.status_code == 200


def test_get_create_purpose(client: TestClient) -> None:
    response: Response = client.get('/purposes/new')
    assert response.status_code == 200


def test_create_purpose(client: TestClient) -> None:
    response: Response = client.post('/purposes/new', data={'user_id': 1, 'purposes': {'math': 5.0}})
    assert response.status_code == 200


def test_edit_purpose(client: TestClient) -> None:
    response: Response = client.put('/purposes/math/edit', data={'user_id': 1, 'subject': 'math', 'purpose': {4.5}})
    assert response.status_code == 200


def test_get_edit_purpose(client: TestClient) -> None:
    response: Response = client.get('/purposes/math/edit')
    assert response.status_code == 200


def test_remove_purpose(client: TestClient) -> None:
    response: Response = client.delete('/purposes/math', data={'user_id': 1, 'subject': 'math'})
    assert response.status_code == 200
