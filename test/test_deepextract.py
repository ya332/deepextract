import os
import unittest
from deepextract import deepextract
# samples taken from here: https://filesamples.com/formats/YAML


class Test(unittest.TestCase):

    def test_json_extract(self):
        json_file_path = os.path.join("data", "test1.json")
        expected_result = [{
            "elements": [{
                "distance": {
                    "text": "94.6 mi",
                    "value": 152193
                },
                "duration": {
                    "text": "1 hour 44 mins",
                    "value": 6227
                },
                "status": "OK"}]}]
        self.assertEqual(deepextract.extract_key_from_file(
            json_file_path, "rows"), expected_result)


        json_file_path = os.path.join("data", "test1.json")
        expected_result = ["New York, NY, USA"]
        self.assertEqual(deepextract.extract_key_from_file(
            json_file_path, "origin_addresses"), expected_result)


        json_file_path = os.path.join("data", "test2.json")
        expected_result = [
            {
                "id": "1001",
                "type": "Regular"
            },
            {
                "id": "1002",
                "type": "Chocolate"
            },
            {
                "id": "1003",
                "type": "Blueberry"
            },
            {
                "id": "1004",
                "type": "Devil's Food"
            }
        ]
        self.assertEqual(deepextract.extract_key_from_file(
            json_file_path, "batter"), expected_result)

    def test_yaml_extract(self):
        yaml_file_path = os.path.join("data", "test1.yaml")
        expected_result = False
        self.assertEqual(deepextract.extract_key_from_file(
            yaml_file_path, "mariadb"), expected_result)


        yaml_file_name = os.path.join('data','test1.yaml')
        expected_result = {"mariadb": False,
                           "ohmyzsh": False,
                           "webdriver": False}
        self.assertEqual(deepextract.extract_key_from_file(
            yaml_file_path, "features"), expected_result)



if __name__ == '__main__':
    unittest.main()
