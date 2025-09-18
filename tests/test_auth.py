import unittest
from fastapi.testclient import TestClient
from app.main import app   #  main.py me app include hona chahiye

client = TestClient(app)

class TestAuth(unittest.TestCase):
    def test_register_user(self):
        response = client.post("/api/auth/register", params={
            "email": "test@example.com",
            "password": "password123"
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"msg": "User registered successfully"})

    def test_login_user(self):
        # Pehle register
        client.post("/api/auth/register", params={
            "email": "testlogin@example.com",
            "password": "password123"
        })
        # Phir login
        response = client.post("/api/auth/login", params={
            "email": "testlogin@example.com",
            "password": "password123"
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn("token", response.json())

if __name__ == "__main__":
    unittest.main()
