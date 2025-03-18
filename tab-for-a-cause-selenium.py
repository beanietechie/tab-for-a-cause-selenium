from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from time import sleep
from sys import stdout

def main():
    stdout.write('=== tab-for-a-cause-selenium ===\n')

    credentialsFile = open('credentials.txt', 'r')
    email = credentialsFile.readline().strip()
    password = credentialsFile.readline().strip()
    stdout.write('credentials read\n')

    driver = webdriver.Firefox()
    stdout.write('browser started\n')

    driver.get('https://tab.gladly.io/newtab/')
    stdout.write('tab for a cause page reached\n')

    wait = WebDriverWait(driver, 15)
    wait.until(lambda driver: driver.current_url == 'https://tab.gladly.io/newtab/auth/?app=tab') # wait for login page to load
    stdout.write('Login page reached, attempting to login.\n')

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
    stdout.write('credentials submitted\n')

    wait.until(lambda driver: driver.current_url == 'https://tab.gladly.io/newtab/') # wait for new tab page to load
    stdout.write('tab for a cause new tab page reached\n')

    while True:
        sleep(4)
        try:
            driver.refresh()
        except WebDriverException:
            stdout.write('refresh failed, continuing, if you see this repeatedly try restarting the program or check your internet connection\n')         

if __name__ == '__main__':
    main()