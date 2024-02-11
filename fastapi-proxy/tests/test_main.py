import pytest 
from httpx import AsyncClient
from main import app

@pytest.mark.asyncio
async def test_translate_text_success():
    async with AsyncClient(app=app, base_url="http://test") as client:
        request_data = {"text": "Hello", "target_lang": "DE"}
        response = await client.post("/translate", json=request_data)
        assert response.status_code == 200
        assert "Hallo" in response.text

@pytest.mark.asyncio
async def test_translate_text_missing_data():
    async with AsyncClient(app=app, base_url="http://test") as client:
        request_data = {"target_lang": "DE"}
        response = await client.post("/translate", json=request_data)
        assert response.status_code == 422  # Unprocessable Entity
