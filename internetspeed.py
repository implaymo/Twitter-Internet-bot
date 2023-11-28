from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv
import time

class InternetSpeed:

    def __init__(self):
        load_dotenv()
        self.email = os.getenv('email')
        self.pw = os.getenv('pw')
        self.user = os.getenv('user')
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get("https://www.speedtest.net/")
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()

        self.downl_speed = 0
        self.upl_speed = 0

    def get_internet_speed(self):
        start_button = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div/div[3]/div/'
                                                          'div/div/div[2]/div[3]/div[1]/a/span[4]')))
        start_button.click()

        time.sleep(90)

        download_speed = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/'
                                                            'div[3]/div[3]/div/div[3]/div/div/'
                                                            'div[2]/div[1]/div[1]/div/div[2]/span')))
        self.downl_speed = download_speed.text


        upload_speed = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div/div[3]/div/div/'
                                                          'div/div[2]/div[3]/div[3]/div/div[3]/'
                                                          'div/div/div[2]/div[1]/div[2]/div/div[2]/span')))
        self.upl_speed = upload_speed.text
