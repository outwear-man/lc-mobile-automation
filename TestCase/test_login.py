from Basic import *

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
    ts=TS()
    wait_Element(driver, config.execute_app).click()
    time.sleep(1)
    wait_Element(driver, '//android.widget.Button[@content-desc="로그인 버튼"]').click()
    time.sleep(5)
    wait_Element(driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.Button').click()
    wait_Element(driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.EditText').send_keys("안추도")
    wait_Element(driver, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.EditText').send_keys("920124")
    wait_Element(driver, '//android.widget.LinearLayout[@content-desc="주민등록번호의 뒷자리 하나를 입력하세요"]').click()

    #----- 주민번호 뒷자리 누르기
    matching = Matching()

    # 스크린샷을 저장할 폴더를 생성합니다.
    currentPath = '%s/' % os.getcwd()
    test_Directory = currentPath + '/'

    if not os.path.exists(test_Directory):
        os.makedirs(test_Directory)

    wait = WebDriverWait(driver, 20)


    # 이미지 찾아 중앙을 tap 한다.
    screenshotPath = test_Directory + '%s-screenshot.png'
    detectImagePath = '/Users/yujin/PycharmProjects/android_auto/assets/1_keypad_login.png'
    driver.save_screenshot(screenshotPath)

    center = matching.detectimage(screenshotPath, detectImagePath)
    driver.tap([center])

    #wait_Elements(driver,'/android.widget.LinearLayout[@content-desc="주민등록번호의 뒷자리 하나를 입력하세요"]/android.widget.FrameLayout/android.widget.EditText').send_keys("2")
    wait_Element(driver, '//android.widget.ImageButton[@content-desc="닫기"]').click()
    wait_Element(driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button').click()
    wait_Element(driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.Button').click()
    wait_Element(driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button').click()
    wait_Element(driver,'//android.widget.EditText[@content-desc="인증 번호 입력"]').send_keys("345665")
    time.sleep(5)

    for i in (0,2):
        wait_Element(driver, '//android.widget.ImageView[@content-desc="1"]').click()
        wait_Element(driver, '//android.widget.ImageView[@content-desc="4"]').click()
        wait_Element(driver, '//android.widget.ImageView[@content-desc="1"]').click()
        wait_Element(driver, '//android.widget.ImageView[@content-desc="4"]').click()
        wait_Element(driver, '//android.widget.ImageView[@content-desc="1"]').click()
        wait_Element(driver, '//android.widget.ImageView[@content-desc="4"]').click()
        time.sleep(1)

    wait_Element(driver, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.Button').click()

    time.sleep(5)
    #카드 비번
    wait_Element(driver, '//android.widget.ImageView[@content-desc="1"]').click()
    wait_Element(driver, '//android.widget.ImageView[@content-desc="2"]').click()
    time.sleep(10)

    wait_Element(driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.Button[1]').click()
    wait_Element(driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ImageView').click()
    wait_Element(driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ImageView[2]').click()

#카드 신청
def test_case_02(driver):
    wait_Element(driver, config.menu_button).click()
    driver.swipe(582, 730, 268, 730, duration=800)
    wait_Element(driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[4]/android.view.View[1]/android.view.View/android.view.View/android.widget.ListView/android.view.View[3]/android.widget.Button').click()
    time.sleep(2)
    wait_Element(driver,'//android.view.View[@content-desc="신용카드"]').click()
    wait_Element(driver,'//android.view.View[@content-desc="LOCA LIKIT 1.2 모든 가맹점 1.2% 할인"]').click()
    wait_Element(driver,'//android.view.View[@content-desc="카드 신청"]').click()






