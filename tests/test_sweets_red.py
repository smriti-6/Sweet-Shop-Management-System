import unittest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

class TestSweetsRed(unittest.TestCase):

    def test_add_sweet(self):
        response = client.post("/sweets", params={
            "name": "Chocolate",
            "category": "Candy",
            "price": 10,
            "quantity": 5
        })
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["name"], "Chocolate")

    def test_get_sweets(self):
        response = client.get("/sweets")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_update_sweet(self):
        # First add a sweet
        add_response = client.post("/sweets", params={
            "name": "Lollipop",
            "category": "Candy",
            "price": 5,
            "quantity": 10
        })
        sweet_id = add_response.json()["id"]

        # Now update it
        update_response = client.put(f"/sweets/{sweet_id}", params={"name": "Updated Lollipop"})
        self.assertEqual(update_response.status_code, 200)
        self.assertEqual(update_response.json()["name"], "Updated Lollipop")

    def test_delete_sweet(self):
        # First add a sweet
        add_response = client.post("/sweets", params={
            "name": "Mango Bar",
            "category": "Candy",
            "price": 15,
            "quantity": 20
        })
        sweet_id = add_response.json()["id"]

        # Now delete it
        delete_response = client.delete(f"/sweets/{sweet_id}")
        self.assertEqual(delete_response.status_code, 200)
        self.assertEqual(delete_response.json()["message"], "Sweet deleted")

    def test_search_sweets(self):
        # Add a sweet
        client.post("/sweets", params={
            "name": "Dark Chocolate",
            "category": "Candy",
            "price": 25,
            "quantity": 7
        })

        # Search
        response = client.get("/sweets/search", params={"name": "Chocolate"})
        self.assertEqual(response.status_code, 200)
        results = response.json()
        self.assertGreaterEqual(len(results), 1)
