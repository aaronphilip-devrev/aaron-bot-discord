import requests
import os

FASTAPI_URL = "http://127.0.0.1:8000"  # Adjust if hosted externally

def post_to_api(endpoint: str, data: dict):
    """
    Send POST request to FastAPI endpoint.
    """
    try:
        response = requests.post(f"{FASTAPI_URL}{endpoint}", json=data)
        return response.json()
    except Exception as e:
        print(f"Error connecting to API: {e}")
        return {"error": "API connection failed"}
