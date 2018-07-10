'''
@author: Julius Loman
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

tenant = "https://xxx1234.live.dynatrace.com/"
username = "john_doe@dynatrace.com"
password = "Passw0rd"
backuri = "#dashboard;id=12345678-abcd-1234-abcd-1234567890ab;gtf=l_30_MINUTES"
wait = 30

if __name__ == '__main__':    
        chrome_options = Options()
        chrome_options.add_argument("--kiosk")
        chrome_options.add_argument("--disable-infobars")
        driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver", chrome_options=chrome_options)
        driver.get(tenant)
        driver.find_element(By.ID, "IDToken1").send_keys(username)
        driver.find_element(By.ID, "formsubmit").click()
        WebDriverWait(driver, wait).until(expected_conditions.presence_of_element_located((By.ID, "IDToken2")))    
        driver.find_element(By.ID, "IDToken2").send_keys(password)
        driver.find_element(By.XPATH, '//*[@id="loginButton_0"]').click()
        WebDriverWait(driver, wait).until(expected_conditions.presence_of_element_located((By.ID, "mobileapp-user-menu")))
        driver.get(tenant+backuri)
        