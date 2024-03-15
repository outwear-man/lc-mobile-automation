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


def test_case_02(driver):
    wait_Element(driver, config.execute_app).click()
    time.sleep(10)
    wait_Element(driver, config.menu_button).click()
    driver.swipe(582, 730, 268, 730, duration=800)
    wait_Element(driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[4]/android.view.View[1]/android.view.View/android.view.View/android.widget.ListView/android.view.View[4]/android.widget.Button').click()
    time.sleep(2)
    wait_Element(driver,'//android.view.View[@content-desc="신용카드"]').click()
    wait_Element(driver,'//android.view.View[@content-desc="LOCA LIKIT 1.2 모든 가맹점 1.2% 할인"]').click()
    wait_Element(driver,'//android.view.View[@content-desc="카드 신청"]').click()