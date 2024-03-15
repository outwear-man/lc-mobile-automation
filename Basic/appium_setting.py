import pytest
import time
import config
import timeEdit
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By

import datetime
# 기다렸다가 클릭하는 함수 wait_Element / wait_Elements


# appium 세팅
@pytest.fixture(scope="module")
def driver():
    capabilities = dict(
        platformName='Android',
        automationName='uiautomator2',
    )
    appium_server_url = 'http://localhost:4723'
    driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
    driver.press_keycode(3)
    yield driver
    driver.quit()

