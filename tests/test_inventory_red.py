import unittest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

class TestInventoryRed(unittest.TestCase):

    def setUp(self):
        # Agar auth token chahiye to yahan se generate ya login karke store kar sakte ho
        self.user_token = "Bearer dummy_user_token"
        self.admin_token = "Bearer dummy_admin_token"

    def test_purchase_sweet_success(self):
        """Test purchasing a sweet decreases its quantity"""
        response = client.post(
            "/api/sweets/1/purchase",
            headers={"Authorization": self.user_token}
        )
        # Failing initially (endpoint not implemented)
        self.assertEqual(response.status_code, 200)

    def test_purchase_sweet_out_of_stock(self):
        """Test purchasing a sweet that is out of stock fails"""
        response = client.post(
            "/api/sweets/999/purchase",
            headers={"Authorization": self.user_token}
        )
        # Failing initially
        self.assertEqual(response.status_code, 400)

    def test_restock_sweet_success(self):
        """Test restocking a sweet increases quantity (admin only)"""
        response = client.post(
            "/api/sweets/1/restock",
            headers={"Authorization": self.admin_token},
            json={"quantity": 10}
        )
        # Failing initially
        self.assertEqual(response.status_code, 200)

    def test_restock_sweet_non_admin(self):
        """Test restocking by non-admin fails"""
        response = client.post(
            "/api/sweets/1/restock",
            headers={"Authorization": self.user_token},
            json={"quantity": 10}
        )
        # Failing initially
        self.assertEqual(response.status_code, 403)

if __name__ == "__main__":
    unittest.main()
