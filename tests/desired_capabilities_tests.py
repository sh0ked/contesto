from contesto.basis.driver_mixin import HttpDriver, IosDriver,QtWebkitDriver
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
        self.assertEqual(desired_capabilities["app"], "/Users/test/app.app", 'wrong app in capabilities in iosdriver')
        self.assertEqual(desired_capabilities["appium-version"], '1.0.0-beta.2', 'wrong appium version in capabilities in iosdriver')
        self.assertEqual(desired_capabilities["name"], "GUI iOS test", 'wrong name in capabilities in iosdriver')
        self.assertEqual(desired_capabilities["platformName"], "iOS", 'wrong platform name in capabilities in iosdriver')
        self.assertEqual(desired_capabilities["deviceName"], "iPhone Simulator", 'wrong device name in capabilities in iosdriver')
        self.assertEqual(desired_capabilities["platformVersion"], 7.1, 'wrong platform version in capabilities in iosdriver')

    def test_http_driver(self):
        driver = HttpDriver()
        driver_settings = getattr(config, driver._driver_type)
        desired_capabilities = driver._form_desired_capabilities(driver_settings)
        self.assertEqual(desired_capabilities["browserName"], "firefox", 'wrong browser in capabilities in httpdriver')
        self.assertEqual(desired_capabilities["version"], "", 'wrong version in capabilities in httpdriver')
        self.assertEqual(desired_capabilities["platform"], "ANY", 'wrong platform in capabilities in httpdriver')

    def test_qtwebkit_driver(self):
        driver = QtWebkitDriver()
        driver_settings = getattr(config, driver._driver_type)
        desired_capabilities = driver._form_desired_capabilities(driver_settings)
        self.assertEqual(desired_capabilities["app"], "/Users/test/app", 'wrong platform in capabilities in qtwebkitdriver')
