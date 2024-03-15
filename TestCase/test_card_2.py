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
    wait_Element(driver, config.execute_app).click()
    time.sleep(5)

    #신분증인증_정보직접입력
#    wait_Element(driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View/android.widget.Button[2]').click()
    #여권/외국인 클
#    wait_Element(driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[1]/android.widget.TabWidget/android.widget.Button[3]').click()
    #여권번호입력
#    wait_Element(driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.widget.EditText').send_keys("M12345678")
#    wait_Element(driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[2]/android.widget.Button').click()

    #결제정보>신청안함
#    wait_Element(driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[1]/android.view.View/android.view.View[3]/android.view.View').click()
    #결제계좌
#    wait_Element(driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[1]/android.view.View/android.widget.Button[3]').click()
#    wait_Element(driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[3]/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View/android.widget.ListView/android.view.View[1]/android.view.View/android.view.View').click()
    #결제계좌입력
#    wait_Element(driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[3]/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText').send_keys(110223232320)
#    wait_Element(driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[3]/android.view.View/android.view.View[2]/android.widget.Button[2]').click()
#    wait_Element(driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[2]/android.widget.Button').click()

    #1원인증건너뛰기, 리볼빙건너뛰기
#    wait_Element(driver,'//android.view.View[@content-desc="건너뛰기"]/android.widget.TextView').click()
#   wait_Element(driver,'//android.view.View[@content-desc="건너뛰기"]/android.widget.TextView').click()

    driver.swipe(300, 1000, 300, 100, duration=800)  # 아래로 스크롤

    #소득유형데이터입력 직장명,전화번호입력
    # wait_Element(driver, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[1]/android.view.View/android.view.View[4]/android.view.View/android.widget.EditText').send_keys("롯데카드")
    # wait_Element(driver, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[1]/android.view.View/android.view.View[5]/android.view.View/android.widget.EditText').send_keys("0255555555")
    wait_Element(driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[1]/android.view.View/android.view.View[4]/android.widget.Button').click()
    driver
    wait_Element(driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View/android.view.View[4]/android.widget.Button')
    wait_Element(driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[3]/android.view.View/android.view.View[2]/android.widget.EditText').send_keys("롯데카드")


    #직장주소_검색
    wait_Element(driver, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[1]/android.view.View/android.view.View[7]/android.widget.Button').click()
    wait_Element(driver, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[3]/android.view.View/android.view.View[2]/android.widget.EditText').send_keys("새문안로76")
    wait_Element(driver, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[3]/android.view.View/android.view.View[2]/android.widget.Button').click() #검색
    time.sleep(3)
    wait_Element(driver, '//android.view.View[@content-desc="03185 서울특별시 종로구 새문안로 76 (신문로1가) 지번서울특별시 종로구 신문로1가 115 콘코디언(concordian)"]/android.widget.TextView[1]').click() #주소리스트클릭
    wait_Element(driver, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[3]/android.view.View/android.view.View[2]/android.widget.Button').click() #주소등록

    #(소득유형데이터완료)다음버튼클릭
    wait_Element(driver, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[2]/android.widget.Button').click()
    #소득확인 건너뛰기
    wait_Element(driver, '//android.view.View[@content-desc="건너뛰기"]').click()
    #배송지선택
    wait_Element(driver, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[1]/android.view.View/android.view.View[2]/android.widget.Button').click() #검색
    wait_Element(driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[3]/android.view.View/android.view.View[2]/android.widget.EditText').send_keys("새문안로76")
    wait_Element(driver, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[3]/android.view.View/android.view.View[2]/android.widget.Button').click()
    wait_Element(driver, '//android.view.View[@content-desc="03185 서울특별시 종로구 새문안로 76 (신문로1가) 지번서울특별시 종로구 신문로1가 115 콘코디언(concordian)"]').click()



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
