# import os
# os.environ['TESTING'] = 'TRUE'

# import unittest
# from unittest import TestCase

from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(ChromeDriverManager().install())


driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.close()




# localHost = "http://localhost:5000/"

# class SeleniumTests(TestCase):

#     def setUp(self):

#         # 初始化 WebDriver
#         self.driver = webdriver.Chrome()

#     def tearDown(self):

#         self.driver.quit()

    
# if __name__ == '__main__':
#     unittest.main()
