from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver import WebElement
from selenium.webdriver.support.wait import WebDriverWait

import os
import cv2
import datetime

# 해당 element가 노출을 sec 초까지 기다리는 함수
# wait_Element 가 기본 5초
def wait_Element_until(driver, xpath, sec):
    location = xpath

    try:
        element:WebElement = WebDriverWait(driver, sec).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        return element

    except TimeoutException:
        print(xpath + " Timeout!!!!!!!!!!!!")
        return False

def wait_Element(driver, xpath):
    location = xpath
    try:
        element:WebElement = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )

        #time.sleep(3)

        return element
    except TimeoutException:
        print("Timeout!!!!!!!!!!!!")
        return False
def wait_Elements(driver, xpath):
    location = xpath
    wait_Element(driver, location)
    return driver.find_elements(By.XPATH, location)

# 현재 화면의 x,y 좌표를 클릭하는 함수
def xyTouch(driver, x, y):
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(x, y)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.pause(0.1)
    actions.w3c_actions.pointer_action.release()
    actions.perform()

# 해당 Xpath 의 x,y 값을 받아오는 함수 x1,y1,x2,y2
def get_xy(driver, xpath):
    bounds = wait_Element(driver, xpath).get_attribute('bounds')

    tmp_1 = bounds.split("][")
    first = tmp_1[0].replace("[","")
    second = tmp_1[1].replace("]","")
    x1 = first.split(",")[0]
    y1 = first.split(",")[1]
    x2 = second.split(",")[0]
    y2 = second.split(",")[1]

    my_dict = {}

    # 키-값 쌍 추가
    my_dict['x1'] = int(x1)
    my_dict['y1'] = int(y1)
    my_dict['x2'] = int(x2)
    my_dict['y2'] = int(y2)

    return my_dict

# 현재 화면에 keyword 가 있는지 확인하는 함수
def keyword_exist(driver, keyword):
    tmp = '//*[contains(@content-desc,"'+keyword+'")]'
    print(tmp)
    return wait_Element(driver, tmp)


def timefunc1():
    testtime=datetime.datetime.now()
    t=testtime.strftime("%Y.%m.%d %H:%M")
    t1=testtime.strftime("%m.%d %H:%M")
    year=t[2:4]
    return_time=year+"."+t1

    return return_time