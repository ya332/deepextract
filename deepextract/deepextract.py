import yaml
import json


def extract_key(obj, target):
    """Recursively fetch values from nested JSON.
        Args:
            obj ([dict]): an arbitrarily nested dictionary with environemt variables
            target (str): The target key we want to extract
        Returns:
            (str | dict): target key can have a string or another dictionary as value in obj. 
        Raises:
            KeyError: if the target is not in the dictionary, raises KeyError.
    """

    if isinstance(obj, dict):
        for k, v in obj.items():

            if k == target:
                return v

            elif isinstance(v, (dict, list)):
                return extract_key(v, target)

    raise KeyError("Key: '{}' not found".format(target))


def extract_key_from_file(file_path_name, target):
    """Recursively fetch values given a file path
    File path can point to a json file or a yaml file.

    Args:
        file_path_name ([type]): [description]
    Returns:
        (str | dict): target key can have a string or another dictionary as value in obj. 
    """
    if "json" in file_path_name:
        obj = read_json_content(file_path_name)
    elif "yaml" or "yml" in file_path_name:
        obj = read_yaml_content(file_path_name)
    return extract_key(obj, target)


def read_yaml_content(yaml_file_name):
    """Return yaml content as a dictionary

    Args:
        filename (str): file name of the yaml file

    Returns:
        dict: Returns yaml content 
    """
    with open(yaml_file_name) as yaml_file:
        yaml_file_content = yaml.full_load(yaml_file)

    return yaml_file_content


def read_json_content(json_file_name):
    """Return json content as a dictionary

    Args:
        json_file_name (str): file name of the json file

    Returns:
        dict: Returns json content 
    Raises:
        FileNotFoundError: raise if json_file_name doens't point to a json file
    """
    f = open(json_file_name)

    try:
        data = json.load(f)  # returns JSON object as a dictionary
    except FileNotFoundError as e:
        raise e
    finally:
        f.close()


def test_env_variables(yaml_file_name):
    """Checks if environment variables are set correctly.

    Args:
        yaml_file_name (str): file name of the yaml file that has environment variables 
    Raises:
        ValueError: raises if environment variable is not successfully.
    """
    yaml_file_content = read_yaml_content(yaml_file_name)
    for key, value in json_extract(yaml_file_content, 'Variables').items():
        if os.environ[key] == str(value):
            print("export {}={}".format(key, value), end="\n")
        else:
            raise ValueError("Setting {}={} failed.".format(key, value))


if __name__ == '__main__':
    set_env_from_yaml("samTemplate-dev.yaml")
