import os
from deepextract import deepextract

# Demo: deepextract.extract_key_from_file(file_path, key) for yaml
json_file_path = os.path.join("..", "data", "test1.yaml")
expected_result = {"mariadb": False,
                   "ohmyzsh": False,
                   "webdriver": False}
print(deepextract.extract_key_from_file(
    json_file_path, "features") == expected_result)

# Demo: deepextract.extract_key_from_file(file_path, key) for json
json_file_path = os.path.join("..", "data", "test1.json")
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
print(deepextract.extract_key_from_file(
    json_file_path, "rows") == expected_result)


# Demo: deepextract.extract_key(obj, key)
deeply_nested_dict = {
    "items": {
        "item": {
            "id": {
                "type": {
                    "donut": {
                        "name": {
                            "batters": {
                                "my_target_key": "my_target_value"
                            }
                        }
                    }
                }
            }
        }
    }
}
print(deepextract.extract_key(deeply_nested_dict, "my_target_key") == "my_target_value")
