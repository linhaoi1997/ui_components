"""复用浏览器调试"""
from selenium import webdriver

from selenium.webdriver import DesiredCapabilities

'''
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome  --remote-debugging-port=8888 --user-data-dir="/Users/linhao/Desktop/linhao/workplace/autoui"
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome  --remote-debugging-port=8889 --user-data-dir="/Users/linhao/Desktop/linhao/workplace/autoui2"
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome  --remote-debugging-port=8890 --user-data-dir="/Users/linhao/Desktop/linhao/workplace/autoui3"
'''


def get_driver(port=8888):
    """拿到打开的浏览器，debug模式，调试用"""
    options = webdriver.ChromeOptions()
    options.add_experimental_option("debuggerAddress", "127.0.0.1:%s" % port)
    c = webdriver.Chrome(port=19888, options=options)
    return c


def get_driver2():
    return get_driver(8889)


def safe_remote_driver():
    from selenium.webdriver.chrome.options import Options
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--window-size=1920x1080')
    chrome_options.add_argument('blink-settings=imagesEnabled=false')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--ignore-certificate-errors')

    caps = DesiredCapabilities.CHROME
    prefs = {
        'profile.default_content_setting_values': {
            'images': 2
        }
    }
    chrome_options.add_experimental_option('prefs', prefs)
    # driver = webdriver.Chrome()
    driver = webdriver.Remote("http://192.168.1.165:4444/wd/hub", options=chrome_options, desired_capabilities=caps)
    return driver


if __name__ == '__main__':
    with safe_remote_driver() as remote_driver:
        remote_driver.get("http://www.baidu.com")
        print(remote_driver.current_url)
        print(remote_driver.find_element_by_id("kw"))
