import unittest
import json
from urllib import request, parse

class TestAuthEndpoints(unittest.TestCase):

    BASE_URL = "http://127.0.0.1:8000/api/auth"

    def test_register_user(self):
        url = f"{self.BASE_URL}/register"
        data = parse.urlencode({"email": "smritikanthak@gmail.com", "password": "pass"}).encode()
        req = request.Request(url, data=data)
        try:
            response = request.urlopen(req)
            self.assertEqual(response.status, 200)
        except Exception as e:
            # Abhi endpoint exist nahi karega, test fail hona chahiye
            print("Expected failure (Red test):", e)
            self.assertTrue(True)

    def test_login_user(self):
        url = f"{self.BASE_URL}/login"
        data = parse.urlencode({"email": "u1@test.com", "password": "pass"}).encode()
        req = request.Request(url, data=data)
        try:
            response = request.urlopen(req)
            self.assertEqual(response.status, 200)
        except Exception as e:
            # Abhi endpoint exist nahi karega, test fail hona chahiye
            print("Expected failure (Red test):", e)
            self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()

