import unittest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

class TestSweetsEdgeRed(unittest.TestCase):

    def test_add_sweet_negative_price(self):
        response = client.post("/api/sweets", json={
            "name": "Chocolate",
            "category": "Candy",
            "price": -10,   # negative price
            "quantity": 5
        })
        # FastAPI/Pydantic validation returns 422 for invalid data
        self.assertEqual(response.status_code, 422)

    def test_add_sweet_negative_quantity(self):
        response = client.post("/api/sweets", json={
            "name": "Candy",
            "category": "Candy",
            "price": 10,
            "quantity": -5  # negative quantity
        })
        self.assertEqual(response.status_code, 422)

    def test_get_sweets_empty(self):
        # No sweets added yet, should return empty list
        response = client.get("/api/sweets")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])

    def test_update_sweet_not_exist(self):
        response = client.put("/api/sweets/999", json={
            "name": "NonExistent"
        })
        self.assertEqual(response.status_code, 404)

    def test_search_no_results(self):
        response = client.get("/api/sweets/search", params={"name": "NonExistingSweet"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])

if __name__ == "__main__":
    unittest.main()
