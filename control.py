from os.path import join
from time import sleep

from selenium import webdriver

from config import Config


config = Config()

def stub_chrome_driver_path():
    """
    MEMO: とりあえず、カレントにchromedrive.exeがある前提でパスを返す
    """
    root = join(__file__, "..")
    driver_path=join(root, "chromedriver.exe")
    return driver_path


def get_driver():
    driver_path = config.chromedriver_path
    options = webdriver.ChromeOptions()
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver = webdriver.Chrome(executable_path=driver_path, options=options)
    return driver


def loopahead(iterable):
    it = iter(iterable)
    last = next(it)
    for val in it:
        yield last, False
        last = val
    # 最後
    yield last, True


def push_btn(interval: int):
    driver = get_driver()

    # TODO: エラーハンドリング
    for xpath, is_end in loopahead(config.xpaths):
        element = driver.find_element_by_xpath(xpath)
        driver.execute_script("arguments[0].click();", element)
        if not(is_end):
            sleep(interval * 60)

