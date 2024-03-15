from Basic import *

# appium 세팅

#opencv 이미지 만들기
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

def test_case_01(driver):
    wait_Element(driver, config.execute_app).click()
    time.sleep(5)
    wait_Element(driver,'//android.widget.RelativeLayout[@content-desc="아직 카드 신청 전인가요?앱을 통해 간편하게 신청해 보세요버튼"]').click()
    time.sleep(5)
    wait_Element(driver,'//android.view.View[@content-desc="LOCA LIKIT 1.2 모든 가맹점 1.2% 할인"]').click()
    wait_Element(driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[3]/android.widget.Button').click()
    time.sleep(10)
    wait_Element(driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[3]/android.widget.Button').click()
    time.sleep(10)
    wait_Element(driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]/android.widget.EditText').send_keys("최텟트")
    wait_Element(driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View/android.view.View[2]/android.widget.EditText').send_keys("TE")
    wait_Element(driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View/android.view.View[3]/android.widget.EditText').send_keys("GDGD")
    wait_Element(driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View/android.view.View[4]/android.widget.EditText[1]').send_keys("900803")
    wait_Element(driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View/android.view.View[4]/android.widget.EditText[2]').click()

    matching=Matching()
    currentPath = '%s/' % os.getcwd()
    test_Directory = currentPath + '/'

    if not os.path.exists(test_Directory):
        os.makedirs(test_Directory)

    wait = WebDriverWait(driver, 20)

    # 이미지 찾아 중앙을 tap 한다.
    screenshotPath = test_Directory + '%s-screenshot.png'
    detectImagePath = ('/Users/channy/PycharmProjects/mobile_auto_test/assets/card_setting_1.png')
    driver.save_screenshot(screenshotPath)

    center = matching.detectimage(screenshotPath, detectImagePath)
    driver.tap([center])
    for i in range(0,6):
        wait_Element(driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View/android.view.View[3]/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.widget.Button[8]').click()

    #전화번호 세팅

    wait_Element(driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View/android.view.View[5]/android.view.View/android.view.View/android.widget.EditText').click()
    wait_Element(driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View/android.view.View[5]/android.view.View/android.view.View/android.widget.EditText').send_keys("01012345678")
    wait_Element(driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View/android.view.View/android.view.View').click()
    wait_Element(driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View/android.view.View[2]/android.widget.Button').click() #다음버튼클릭


    # #신분증인증_정보직접입력
    # wait_Element(driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View/android.view.View/android.widget.Button[2]').click()
    # #여권/외국인 클
    # wait_Element(driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[1]/android.widget.TabWidget/android.widget.Button[3]').click()
    # #여권번호입력
    # wait_Element(driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.widget.EditText').send_keys("M12345678")






    #wait_Element(driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View/android.view.View[5]/android.view.View/android.view.View/android.widget.EditText').click()
    # #이미지 찾기로 해볼까..
    # currentPath = '%s/' % os.getcwd()
    # test_Directory = currentPath + '/'
    #
    # if not os.path.exists(test_Directory):
    #     os.makedirs(test_Directory)
    #
    # wait = WebDriverWait(driver, 20)
    #
    # # 이미지 찾아 중앙을 tap 한다.
    # screenshotPath = test_Directory + '%s-screenshot.png'
    # detectImagePath = '/Users/yujin/PycharmProjects/android_auto/assets/phone_0.png'
    # driver.save_screenshot(screenshotPath)
    #
    # center = matching.detectimage(screenshotPath, detectImagePath)
    # driver.tap([center])
    #
    # currentPath = '%s/' % os.getcwd()
    # test_Directory = currentPath + '/'
    #
    # if not os.path.exists(test_Directory):
    #     os.makedirs(test_Directory)
    #
    # wait = WebDriverWait(driver, 20)
    #
    # # 이미지 찾아 중앙을 tap 한다.
    # screenshotPath = test_Directory + '%s-screenshot.png'
    # detectImagePath = '/Users/yujin/PycharmProjects/android_auto/assets/phone_1.png'
    # driver.save_screenshot(screenshotPath)
    #
    # center = matching.detectimage(screenshotPath, detectImagePath)
    # driver.tap([center])
    #
    # currentPath = '%s/' % os.getcwd()
    # test_Directory = currentPath + '/'
    #
    # if not os.path.exists(test_Directory):
    #     os.makedirs(test_Directory)
    #
    # wait = WebDriverWait(driver, 20)
    #
    # # 이미지 찾아 중앙을 tap 한다.
    # screenshotPath = test_Directory + '%s-screenshot.png'
    # detectImagePath = '/Users/yujin/PycharmProjects/android_auto/assets/phone_8.png'
    # driver.save_screenshot(screenshotPath)
    #
    # center = matching.detectimage(screenshotPath, detectImagePath)
    # driver.tap([center])
    #
    # currentPath = '%s/' % os.getcwd()
    # test_Directory = currentPath + '/'
    #
    # if not os.path.exists(test_Directory):
    #     os.makedirs(test_Directory)
    #
    # wait = WebDriverWait(driver, 20)
    #
    # # 이미지 찾아 중앙을 tap 한다.
    # screenshotPath = test_Directory + '%s-screenshot.png'
    # detectImagePath = '/Users/yujin/PycharmProjects/android_auto/assets/phone_5.png'
    # driver.save_screenshot(screenshotPath)
    #
    # center = matching.detectimage(screenshotPath, detectImagePath)
    # for i in range(0,7):
    #     driver.tap([center])
    #wait_Element(driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View/android.view.View[5]/android.view.View/android.view.View/android.widget.EditText').click()
    #wait_Element(driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[1]/android.view.View/android.view.View[5]/android.view.View/android.widget.Button').click()
    wait_Element(driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.widget.Button').click()
    wait_Element(driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View/android.view.View[2]/android.widget.Button').click()
    wait_Element(driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[3]/android.view.View/android.view.View[2]/android.widget.ListView/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View').click()
    wait_Element(driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[3]/android.view.View/android.widget.Button').click()
    wait_Element(driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View/android.view.View[4]').click()
    wait_Element(driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[3]/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText').send_keys("343434")
    wait_Element(driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[2]/android.widget.Button').click()
    wait_Element(driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[3]/android.view.View/android.widget.Button').click()
    wait_Element(driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[1]/android.widget.Button').click()
