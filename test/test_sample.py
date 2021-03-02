import unittest
from deepextract import deepextract
 # samples taken from here: https://filesamples.com/formats/YAML

class Test(unittest.TestCase):

    def test_yaml_extract(self):
        deepextract.set_env_from_yaml('../data/invoice.yml')
        

if __name__ == '__main__':
    unittest.main()
