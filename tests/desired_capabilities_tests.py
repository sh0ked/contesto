from contesto.basis.driver_mixin import HttpDriver, IosDriver, QtWebkitDriver
from contesto import config
import os
import unittest


class DesireCapabilitiesTestCase(unittest.TestCase):

    def setUp(self):
        config.add_config_file(os.path.abspath(os.path.dirname(__file__)) + "/data/config/drivers.ini")

    def test_ios_driver(self):
        driver = IosDriver()
        driver_settings = getattr(config, driver._driver_type)
        desired_capabilities = driver._form_desired_capabilities(driver_settings)
        dc = {
            'app': '/Users/test/app.app',
            'device': 'iPhone Simulator',
            'platform': 'Mac',
            'version': 7.0,
        }
        self.assertDictEqual(desired_capabilities, dc, 'wrong params in capabilities in iosdriver')

    def test_http_driver(self):
        driver = HttpDriver()
        driver_settings = getattr(config, driver._driver_type)
        desired_capabilities = driver._form_desired_capabilities(driver_settings)
        dc = {
            "platform": 'ANY',
            'javascriptEnabled': True,
            'platform': 'ANY',
            'browserName': 'firefox',
            'version': '',
            'browser': 'firefox'
        }
        self.assertDictEqual(desired_capabilities, dc, 'wrong params in capabilities in httpdriver')

    def test_qtwebkit_driver(self):
        driver = QtWebkitDriver()
        driver_settings = getattr(config, driver._driver_type)
        desired_capabilities = driver._form_desired_capabilities(driver_settings)
        dc = {
            'app': '/Users/test/app',
        }
        self.assertDictEqual(desired_capabilities, dc, 'wrong params in capabilities in qtwebkitdriver')
