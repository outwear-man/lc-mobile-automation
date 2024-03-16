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


def execute_opencv(driver):
    matching=Matching()
    currentPath = '%s/' % os.getcwd()
    test_Directory = currentPath + '/'

    if not os.path.exists(test_Directory):
        os.makedirs(test_Directory)

    wait = WebDriverWait(driver, 20)

    # 이미지 찾아 중앙을 tap 한다.
    screenshotPath = test_Directory + '%s-screenshot.png'
    detectImagePath = '/Users/yujin/PycharmProjects/android_auto/assets/card_setting.png'
    driver.save_screenshot(screenshotPath)

    center = matching.detectimage(screenshotPath, detectImagePath)
    return center