import unittest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

class TestSweetsEdgeRed(unittest.TestCase):

    def test_add_sweet_negative_price(self):
        response = client.post("/sweets", params={
            "name": "Bad Sweet",
            "category": "Candy",
            "price": -10,
            "quantity": 5
        })
        self.assertEqual(response.status_code, 400)

    def test_add_sweet_negative_quantity(self):
        response = client.post("/sweets", params={
            "name": "Weird Sweet",
            "category": "Candy",
            "price": 5,
            "quantity": -3
        })
        self.assertEqual(response.status_code, 400)

    def test_update_nonexistent_sweet(self):
        response = client.put("/sweets/999", params={"name": "Ghost Sweet"})
        self.assertEqual(response.status_code, 404)

    def test_delete_nonexistent_sweet(self):
        response = client.delete("/sweets/999")
        self.assertEqual(response.status_code, 404)

    def test_search_no_results(self):
        response = client.get("/sweets/search", params={"name": "Blueberry Candy"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])
