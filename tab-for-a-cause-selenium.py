from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from time import sleep
import os

def main():
    print('=== tab-for-a-cause-selenium ===')

    credentialsFile = open('credentials.txt', 'r')
    email = credentialsFile.readline().strip()
    password = credentialsFile.readline().strip()
    print('credentials read')

    driver = webdriver.Firefox()
    print('browser started')

    driver.get('https://tab.gladly.io/newtab/')
    print('tab for a cause page reached')

    wait = WebDriverWait(driver, 15)
    wait.until(lambda driver: driver.current_url == 'https://tab.gladly.io/newtab/auth/?app=tab') # wait for login page to load
    print('Login page reached, attempting to login.')

    loginBtn = wait.until(lambda driver: driver.find_element(By.CLASS_NAME, 'firebaseui-idp-password')) # wait for login button to load
    loginBtn.click()
    emailTxt = wait.until(lambda driver: driver.find_element(By.ID, 'ui-sign-in-email-input')) # wait for email input to load
    emailTxt.send_keys(email)
    submitBtn = wait.until(lambda driver: driver.find_element(By.CLASS_NAME, 'firebaseui-id-submit')) # wait for submit button to load
    submitBtn.click()
    passwordTxt = wait.until(lambda driver: driver.find_element(By.ID, 'ui-sign-in-password-input')) # wait for password input to load
    passwordTxt.send_keys(password)
    submitBtn = wait.until(lambda driver: driver.find_element(By.CLASS_NAME, 'firebaseui-id-submit')) # wait for submit button to load
    submitBtn.click()
    print('credentials submitted')

    wait.until(lambda driver: driver.current_url == 'https://tab.gladly.io/newtab/') # wait for new tab page to load
    print('tab for a cause new tab page reached')

    while True:
        sleep(4)
        try:
            driver.refresh()
        except WebDriverException:
            print('refresh failed, continuing, if you see this repeatedly try restarting the program or check your internet connection')         

if __name__ == '__main__':
    main()