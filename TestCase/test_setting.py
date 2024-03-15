from Basic import *

#  설정 메뉴 이동 확인(PJ50-536)
def test_case_01(driver)->None:
    wait_Element(driver, config.execute_app).click()
    time.sleep(10)
    wait_Element(driver, config.menu_button).click()
    wait_Element(driver, config.setting_button).click()
# 앱 최신정보 확인(PJ50-594)
def test_case_02(driver)->None:
    time.sleep(3)
    driver.swipe(300, 1000, 300, 100, duration=800)
    version=driver.find_element(By.XPATH, config.version_text).text
    assert version == config.current_ver, "true"
# 내 정보 관리 변경
def test_case_03(driver)->None:
    wait_Element(driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ImageButton').click()
    wait_Element(driver, '//android.view.View[@content-desc="내정보관리"]').click()
    time.sleep(3)
    wait_Element(driver, '//android.view.View[@content-desc="서류발급신청"]').click()
    wait_Element(driver, '//android.widget.ImageView[@content-desc="1"]').click()
    wait_Element(driver, '//android.widget.ImageView[@content-desc="4"]').click()
    wait_Element(driver, '//android.widget.ImageView[@content-desc="1"]').click()
    wait_Element(driver, '//android.widget.ImageView[@content-desc="4"]').click()
    wait_Element(driver, '//android.widget.ImageView[@content-desc="1"]').click()
    wait_Element(driver, '//android.widget.ImageView[@content-desc="4"]').click()


# # def test_case_03(driver):
# #     time.sleep(2)
#
#     # 자동 입력할 아이디와 비밀번호
#     username_text = "kchan3534"
#     password_text = "cksdms!23"
#
#     # 아이디 입력
#     username_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText"
#     username_field = driver.find_element(By.XPATH, username_xpath)
#     username_field.send_keys(username_text)
    # # 비밀번호 입력
    # password_xpath = "//android.widget.EditText[@content-desc='비밀번호 입력']"
    # password_field = driver.find_element(By.XPATH, password_xpath)
    # password_field.send_keys(password_text)
