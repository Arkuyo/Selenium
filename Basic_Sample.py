# coding=utf-8
"""
Selenium基本範例
@Author: Arkuyo

"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
import time
import re


class Sample(unittest.TestCase):
    def setUp(self):   # 每個Test Case一開始的操作
        # web driver後面可替換不同瀏覽器，後方為driver存放路徑放置
        self.driver = webdriver.Chrome(executable_path=r'D:\WebDriver\chromedriver.exe')   # Google Chrome
        # self.driver = webdriver.Edge(executable_path=r'D:\WebDriver\MicrosoftWebDriver.exe')   # IE Edge
        # self.driver = webdriver.Firefox(executable_path=r'D:\WebDriver\geckodriver.exe')   # FiexFox
        # self.driver = webdriver.Opera(executable_path=r'D:\WebDriver\operadriver.exe')   # Opera
        self.driver.implicitly_wait(30)   # 隱性等待
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_a1_google_search(self):
        driver = self.driver
        driver.get("https://www.google.com.tw/")   # 取得網站位置
        driver.find_element_by_name("q").clear()   # 找到該元素位置，做後續操作
        driver.find_element_by_name("q").send_keys(u"wiki")
        driver.find_element_by_name("q").send_keys(Keys.ENTER)
        driver.find_element_by_partial_link_text("wiki").click()   # 網頁上點擊結字串
        print("Element found by link text!")

        url = driver.current_url   # 將目前網址存起來，比對用
        # 最後一定要有斷言應用，已確認最後結果是否符合預期結果，來判斷Pass/Fail
        self.assertEqual(url, "https://zh.wikipedia.org/wiki/Wiki")   # 斷言應用，比對網址是否正確，來判斷有無成功
        print("Success ...!\\n")

    def test_a2_undefined_testcase(self):
        print(" Start here... ")
        """
        請將欲操作的步驟寫入其中 ...
        ...
        ...
        
        """
        print("End here...")

    # 可判斷某元素是否存在
    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            print(e)
            return False
        return True

    # 可判斷是否跳出警告視窗
    def is_alert_present(self):
        try:
            self.driver.switch_to.alert()
        except NoAlertPresentException as e:
            print(e)
            return False
        return True

    # 關閉警告視窗，並且存取文字
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):   # 每個Test Case結尾的操作
        self.driver.quit()   # 關閉瀏覽器
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
