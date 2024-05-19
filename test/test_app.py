from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import UnexpectedAlertPresentException
import time

def test_homepage_title():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920x1080')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=options)
    try:
        driver.get("http://localhost:5000/")
        WebDriverWait(driver, 10).until(EC.title_contains("QuorAI - Answers with AI"))
        assert "QuorAI - Answers with AI" in driver.title
        print("Homepage title is correct.")
    finally:
        driver.quit()

def test_login():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920x1080')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=options)
    try:
        driver.get("http://localhost:5000/")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "loginButton")))

        login_button = driver.find_element(By.ID, "loginButton")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "loginButton")))
        login_button.click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "InputUsername")))

        username_field = driver.find_element(By.ID, "InputUsername")
        password_field = driver.find_element(By.ID, "InputPassword1")

        username_field.send_keys("aaa")  # 修改为实际用户名
        password_field.send_keys("aaa")  # 修改为实际密码

        actual_login_button = driver.find_element(By.XPATH, "//button[@class='btn btn-primary' and @onclick='submitLoginForm()']")
        actual_login_button.click()

        try:
            # 等待警告对话框出现
            WebDriverWait(driver, 10).until(EC.alert_is_present())

            # 切换到警告对话框并获取文本
            alert = driver.switch_to.alert
            alert_text = alert.text
            print(f"Alert Text: {alert_text}")

            # 接受警告对话框
            alert.accept()

            # 检查警告文本
            if "Login successful!" in alert_text:
                print("Login test passed.")
            else:
                print("Login test failed: Unexpected alert text.")
                assert False, "Login failed with unexpected alert text."
        except UnexpectedAlertPresentException as e:
            print(f"An error occurred: {e}")
            raise

    finally:
        driver.quit()

def test_register():
    driver = webdriver.Chrome()
    try:
        driver.get("http://localhost:5000/")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "registerbtn")))

        Register_button = driver.find_element(By.ID, "registerbtn")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "registerbtn")))
        Register_button.click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "InputUsernameR")))
        username_field = driver.find_element(By.ID, "InputUsernameR")  # 更新为注册表单中的用户名输入框ID
        email_field = driver.find_element(By.ID, "InputEmail1R")  # 更新为注册表单中的邮箱输入框ID
        password_field1 = driver.find_element(By.ID, "InputPassword3R")  # 更新为注册表单中的密码输入框ID
        checkbox = driver.find_element(By.ID, "invalidCheck")

        username_field.send_keys("aaa")  # 修改为实际用户名
        email_field.send_keys("test111@example.com")  # 修改为实际邮箱
        password_field1.send_keys("aaa")  # 修改为实际密码

        checkbox.click()
        
        actual_register_button = driver.find_element(By.NAME, "submitR")  # 更新为注册表单中的注册按钮ID
        actual_register_button.click()

        # 等待注册成功的提示
        try:
            # 等待警告对话框出现
            WebDriverWait(driver, 10).until(EC.alert_is_present())

            # 切换到警告对话框并获取文本
            alert = driver.switch_to.alert
            alert_text = alert.text
            print(f"Alert Text: {alert_text}")

            # 接受警告对话框
            alert.accept()

            # 检查警告文本
            if "User registered successfully!" in alert_text:
                print("Register test passed.")
            else:
                print("Register test failed: Unexpected alert text.")
                assert False, "Register failed with unexpected alert text."
        except UnexpectedAlertPresentException as e:
            print(f"An error occurred: {e}")
            raise

    finally:
        driver.quit()




if __name__ == "__main__":
    test_homepage_title()
    test_register()
    test_login()