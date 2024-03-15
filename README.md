# 구조
- 테스트 프레임워크 : Appium, pytest
- 롯데카드 앱이 홈화면에 있는 상태에서 구동 가능

# 사전설치 1. Appium
1. Appium 설치 및 실행
- http://appium.io/docs/en/2.1/quickstart/install/ 참고

2. Appium Driver 설치
```
#Install
npm i -g appium
appium driver install uiautomator2
appium driver install xcuitest

#Run
appium
```
# 사전설치 2 pip
```
pip install pytest
pip install Appium-Python-Client
pip install selenium
```

# 실행
- pytest 명령어를 통해서 실행 시, test_ 로 시작하는 모든 테스트 파일 실행
```
pytest -s
```

- 특정 파일만 테스트 하고 싶다면
```
pytest test_case_01.py -s
```


# 리포트 보기
```
jenkin + allure 리포트 연동 예정
```

# 파일구조
```
├── Basic
│   └── appium_setting.py : appium을 통한 모바일 기기 구동
│   └── common.py : 자주 사용하는 함수 모음
│   └── config.py : xPath or 환경변수 모음
├── TestCase
│   ├── test_01_... :
│   ├── test_02_... :
│   ├── test_03_... :
│   ├── test_04_... :
```
