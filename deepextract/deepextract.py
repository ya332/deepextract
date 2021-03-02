import yaml
import os

def json_extract(obj, target):
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

            elif isinstance(v, dict):
                return json_extract(v, target)
            
    raise KeyError("Key: '{}' not found".format(target))


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

def set_env_from_yaml(yaml_file_name):
    """Set environment variables from yaml file.

    Args:
        yaml_file_name (str): file name of the yaml file that has environment variables
    """
    yaml_file_content = read_yaml_content(yaml_file_name)
    for key, value in json_extract(yaml_file_content, 'Variables').items():
        os.environ[key] = str(value)

    test_env_variables(yaml_file_name)

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
    