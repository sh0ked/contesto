from contesto.exceptions import UnknownBrowserName
from selenium.webdriver import DesiredCapabilities


class AbstractDriver(object):
    _driver_type = None
    dc_from_config = None

    @classmethod
    def _form_desired_capabilities(cls, driver_settings):
        try:
            cls.dc_from_config = driver_settings["desired_capabilities"]
        except KeyError:
            pass


class HttpDriver(AbstractDriver):
    capabilities_map = {
        "firefox": DesiredCapabilities.FIREFOX,
        "internet explorer": DesiredCapabilities.INTERNETEXPLORER,
        "chrome": DesiredCapabilities.CHROME,
        "opera": DesiredCapabilities.OPERA,
        "safari": DesiredCapabilities.SAFARI,
        "htmlunit": DesiredCapabilities.HTMLUNIT,
        "htmlunitjs": DesiredCapabilities.HTMLUNITWITHJS,
        "iphone": DesiredCapabilities.IPHONE,
        "ipad": DesiredCapabilities.IPAD,
        "android": DesiredCapabilities.ANDROID,
        "phantomjs": DesiredCapabilities.PHANTOMJS,
        ### aliases:
        "ff": DesiredCapabilities.FIREFOX,
        "internetexplorer": DesiredCapabilities.INTERNETEXPLORER,
        "iexplore": DesiredCapabilities.INTERNETEXPLORER,
        "ie": DesiredCapabilities.INTERNETEXPLORER,
        "phantom": DesiredCapabilities.PHANTOMJS,
    }
    _driver_type = 'selenium'

    @classmethod
    def _form_desired_capabilities(cls, driver_settings):
        super(HttpDriver, cls)._form_desired_capabilities(driver_settings)
        if cls.dc_from_config:
            try:
                desired_capabilities = cls.capabilities_map[cls.dc_from_config["browserName"].lower()].copy()
            except KeyError:
                raise UnknownBrowserName(cls.dc_from_config["browserName"], cls.capabilities_map.keys())

            cls.dc_from_config['browserName'] = desired_capabilities['browserName']
            desired_capabilities.update(cls.dc_from_config)

            return desired_capabilities

        else:
            ### for backward compatibility
            try:
                desired_capabilities = cls.capabilities_map[driver_settings["browser"].lower()].copy()
            except KeyError:
                raise UnknownBrowserName(driver_settings["browser"], cls.capabilities_map.keys())

            for key, value in driver_settings.iteritems():
            ### todo IEDriver becomes insane with host/port parameters in desired_capabilities, need investigation
                if key not in ('host', 'port'):
                    desired_capabilities[key] = value

            return desired_capabilities


class QtWebkitDriver(AbstractDriver):
    _driver_type = 'qtwebkitdriver'

    @classmethod
    def _form_desired_capabilities(cls, driver_settings):
        super(QtWebkitDriver, cls)._form_desired_capabilities(driver_settings)
        if cls.dc_from_config:
            return cls.dc_from_config

        desired_capabilities = dict()
        desired_capabilities['app'] = driver_settings["app"]
        return desired_capabilities


class IosDriver(AbstractDriver):
    _driver_type = 'iosdriver'

    @classmethod
    def _form_desired_capabilities(cls, driver_settings):
        super(IosDriver, cls)._form_desired_capabilities(driver_settings)
        if cls.dc_from_config:
            return cls.dc_from_config

        desired_capabilities = dict()
        desired_capabilities['app'] = driver_settings["app"]
        desired_capabilities['device'] = driver_settings["device"]
        desired_capabilities['platform'] = driver_settings["platform"]
        desired_capabilities['version'] = driver_settings["version"]
        return desired_capabilities