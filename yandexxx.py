import unittest
import requests


class TestYandexDiskAPI(unittest.TestCase):

    def setUp(self):
        self.token = "токен"
        self.headers = {
            "Authorization": f"OAuth {self.token}",
            "Content-Type": "application/json"
        }
        self.base_url = "https://cloud-api.yandex.net/v1/disk/resources"
        self.folder_name = "test_folder"

    def test_create_folder_success(self):
        requests.delete(self.base_url, headers=self.headers, params={"path": self.folder_name})
        response = requests.put(self.base_url, headers=self.headers, params={"path": self.folder_name})
        self.assertEqual(response.status_code, 201)

    def test_create_folder_already_exists(self):
        requests.put(self.base_url, headers=self.headers, params={"path": self.folder_name})
        response = requests.put(self.base_url, headers=self.headers, params={"path": self.folder_name})
        self.assertEqual(response.status_code, 409)

    def test_create_folder_invalid_token(self):
        bad_headers = {"Authorization": "OAuth wrong_token", "Content-Type": "application/json"}
        response = requests.put(self.base_url, headers=bad_headers, params={"path": self.folder_name})
        self.assertEqual(response.status_code, 401)

    def test_create_folder_empty_name(self):
        response = requests.put(self.base_url, headers=self.headers, params={"path": ""})
        self.assertEqual(response.status_code, 400)

    def tearDown(self):
        try:
            requests.delete(self.base_url, headers=self.headers, params={"path": self.folder_name})
        except:
            pass


if __name__ == '__main__':
    unittest.main()