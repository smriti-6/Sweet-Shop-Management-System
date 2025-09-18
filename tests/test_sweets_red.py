import unittest
from app.main import app

class TestSweetsRed(unittest.TestCase):
    
    def test_add_sweet(self):
        """Test adding a new sweet (should fail, endpoint not implemented)"""
        response = app.add_sweet(name="Chocolate", category="Candy", price=10, quantity=5)
        self.assertEqual(response["msg"], "Sweet added successfully")
    
    def test_get_sweets(self):
        """Test retrieving all sweets (should fail)"""
        response = app.get_sweets()
        self.assertIsInstance(response, list)
    
    def test_update_sweet(self):
        """Test updating sweet details (should fail)"""
        response = app.update_sweet(1, name="Dark Chocolate")
        self.assertEqual(response["msg"], "Sweet updated successfully")
    
    def test_delete_sweet(self):
        """Test deleting a sweet (should fail)"""
        response = app.delete_sweet(1)
        self.assertEqual(response["msg"], "Sweet deleted successfully")
    
    def test_search_sweets(self):
        """Test searching sweets (should fail)"""
        response = app.search_sweets(name="Chocolate")
        self.assertGreaterEqual(len(response), 1)

if __name__ == "__main__":
    unittest.main()
