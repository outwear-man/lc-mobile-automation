from appium.webdriver.common.appiumby import AppiumBy

from Basic import *

class TS():
    def makeTS(self):
        return str(int(datetime.datetime.now().timestamp()))

class Matching():

    def detectimage(self, screenshotPath, detectImagePath):

        sourceimage = cv2.imread(screenshotPath, 0)
        template = cv2.imread(detectImagePath, 0)

        w, h = template.shape[::-1]

        method = eval('cv2.TM_CCOEFF')
        res = cv2.matchTemplate(sourceimage, template, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        print('max_val: %d' % max_val)

        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        center = (top_left[0] + int(w/2), top_left[1] + int(h/2))

        color = (0, 0, 255)
        cv2.rectangle(sourceimage, top_left, bottom_right, color, thickness=8)

        detectshotPath = screenshotPath[:-4] + '-detect.png'
        cv2.imwrite(detectshotPath, sourceimage)

        return center

def test_case_01(driver)->None :
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@content-desc="Chrome"]').click()
    time.sleep(2)
    #driver.find_element(by=AppiumBy.ID, value='com.android.chrome:id/search_box_text').click()
    #driver.find_element(by=AppiumBy.XPATH,value='//android.view.View[@content-desc="124.243.36.17(안전하지 않음)"]/android.widget.TextView').click()
    driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="[인증_POPUP]"]/android.widget.TextView').click()
    time.sleep(3)
    driver.find_element(by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.widget.Button').click()
    #driver.find_element(by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.widget.Button').click()
    time.sleep(5)
    driver.find_element(by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button').click()
    time.sleep(2)
    #간편번호 입력
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ImageView[@content-desc="1"]').click()
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ImageView[@content-desc="4"]').click()
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ImageView[@content-desc="1"]').click()
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ImageView[@content-desc="4"]').click()
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ImageView[@content-desc="1"]').click()
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ImageView[@content-desc="4"]').click()
    time.sleep(5)


    driver.find_element(by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button').click()
    #driver.find_element(by=AppiumBy.XPATH, value='//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button').click()
    time.sleep(5)
    #승인 버튼
    driver.swipe(300, 1500, 300, 100, duration=800)

    matching = Matching()
    # 스크린샷을 저장할 폴더를 생성합니다.
    currentPath = '%s/' % os.getcwd()
    test_Directory = currentPath + '/'

    if not os.path.exists(test_Directory):
        os.makedirs(test_Directory)

    wait = WebDriverWait(driver, 20)


    # 이미지 찾아 중앙을 tap 한다.
    screenshotPath = test_Directory + '%s-screenshot.png'
    detectImagePath = '/Users/yujin/PycharmProjects/android_auto/assets/pay_apply.png'
    driver.save_screenshot(screenshotPath)

    center = matching.detectimage(screenshotPath, detectImagePath)
    driver.tap([center])

    #앱 이용 내역 확인
    date = timefunc1()
    wait_Element(driver, config.execute_app).click()
    time.sleep(10)
    driver.find_element(by=AppiumBy.XPATH,value='//android.view.View[@content-desc="내 카드 1개 실적•혜택보기 최근이용내역 보러가기 내 이용한도 확인하기"]/android.view.View[2]/android.view.View').click()
    pay_date=driver.find_element(by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.widget.ListView[1]/android.view.View[1]/android.view.View/android.widget.ListView/android.view.View[2]/android.widget.ListView/android.view.View[1]').text()
    assert date==pay_date, "true"