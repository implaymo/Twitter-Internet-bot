from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv



class Twitter:
    def __init__(self):
        load_dotenv()
        self.email = os.getenv('email')
        self.pw = os.getenv('pw')
        self.user = os.getenv('user')
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get("https://twitter.com/home")
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()


    def sign_in_twitter(self):
        username_input = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/'
                                                      'div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')))
        username_input.send_keys(f"{self.user}")

        next_button = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/'
                                                      'div[2]/div/div/div[2]/div[2]/'
                                                      'div/div/div/div[6]/div/span/span')))
        next_button.click()

        password = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/'
                                                      'div/div[2]/div[2]/div[1]/div/div/div[3]/'
                                                      'div/label/div/div[2]/div[1]/input')))
        password.send_keys(f"{self.pw}")
        login_button = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/'
                                                      'div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div')))
        login_button.click()

    def write_tweet(self):
        pass