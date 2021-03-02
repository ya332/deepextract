import unittest
 # samples taken from here: https://filesamples.com/formats/YAML

class Test(unittest.TestCase):

    def test_yaml_extract(self):
        self.assertEqual(add_one(5), 6)


if __name__ == '__main__':
    unittest.main()
