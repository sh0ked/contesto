import os
import unittest
from contesto import config
from contesto.utils.lambda_object import LambdaObject


class ConfigTest(unittest.TestCase):
    def test_default_config(self):
        default = LambdaObject()
        default.selenium = {
            "host": "localhost",
            "port": 4444,
            "browser": "firefox",
            "platform": "ANY",
        }
        default.timeout = {"normal": 5, }
        default.session = {"shared": False, }
        default.sizzle = {"url": "http://cdnjs.cloudflare.com/ajax/libs/sizzle/1.10.14/sizzle.min.js", }

        for key, value in vars(default).iteritems():
            for k, v in value.iteritems():
                actual = getattr(config, key)[k]
                expected = v
                self.assertEqual(type(actual), type(expected))
                self.assertEqual(actual, expected)

    def test_override_params(self):
        ### @todo mock config files (data/config/*.ini)
        config.add_config_file(os.path.abspath(os.path.dirname(__file__)) + "/data/config/override.ini")
        self.assertEqual(config.selenium["browser"], "ie")

    def test_add_params(self):
        ### @todo mock config files (data/config/*.ini)
        config.add_config_file(os.path.abspath(os.path.dirname(__file__)) + "/data/config/addition.ini")
        self.assertEqual(config.timeout["max"], 30)
        self.assertEqual(config.section["param"], "value")

    def test_complex_param(self):
        ### @todo mock config files (data/config/*.ini)
        config.add_config_file(os.path.abspath(os.path.dirname(__file__)) + "/data/config/complex.ini")
        self.assertEqual(config.complex["int"], 42)
        self.assertEqual(config.complex["float"], 2.718)
        self.assertEqual(config.complex["string"], "3.14")
        self.assertTrue(config.complex["bool"])
        self.assertEqual(config.complex["dict"], {"a": 1, "b": 2})
        self.assertEqual(config.complex["list"], [1, 2, 3])
