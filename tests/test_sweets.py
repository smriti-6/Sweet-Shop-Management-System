import unittest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

class TestSweets(unittest.TestCase):
    
    def test_add_sweet_fail(self):
        # Red test: Endpoint should fail because we haven't implemented it yet
        response = client.post("/api/sweets", json={
            "name": "Ladoo",
            "category": "Indian",
            "price": 10.0,
            "quantity": 50
        })
        self.assertNotEqual(response.status_code, 200)  # Expect failure

    def test_get_sweets_fail(self):
        response = client.get("/api/sweets")
        self.assertNotEqual(response.status_code, 200)  # Expect failure

    def test_search_sweets_fail(self):
        response = client.get("/api/sweets/search?name=Ladoo")
        self.assertNotEqual(response.status_code, 200)  # Expect failure

    def test_update_sweet_fail(self):
        response = client.put("/api/sweets/1", json={"price": 15.0})
        self.assertNotEqual(response.status_code, 200)  # Expect failure

    def test_delete_sweet_fail(self):
        response = client.delete("/api/sweets/1")
        self.assertNotEqual(response.status_code, 200)  # Expect failure

if __name__ == "__main__":
    unittest.main()
