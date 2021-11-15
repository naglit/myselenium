from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from util.config import Config

class SeleniumUtil:

    @staticmethod
    def get_driver(is_mobile_emu = False):
        chrome_options = Options()

        # keep the browser open
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("--start-maximized")
        if (is_mobile_emu):
            mobile_emulation = { 
                "deviceName": "iPhone X"    
                # Or specify a specific build using the following two arguments
                #"deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },
                #"userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19" }
            }
            chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
            
        # ignore insecure certs alert
        capabilities = DesiredCapabilities.CHROME.copy()
        capabilities['acceptInsecureCerts'] = True

        # get a driver
        driver = webdriver.Chrome(
            executable_path=SeleniumUtil.__get_driver_path(),
            desired_capabilities=capabilities,
            options=chrome_options
        )
        return driver

    @staticmethod
    def __get_driver_path():
        config_file = Config.get_config_file()
        driver_path = config_file["selenium_driver_path"]
        return driver_path
        