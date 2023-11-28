from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv
from internetspeed import InternetSpeed


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

        self.internet_speed = InternetSpeed()
        self.internet_speed.get_internet_speed()

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

    def post_tweet_button(self):
        post_button = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/'
                                                         'div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/'
                                                         'div[2]/div[2]/div/div/div/div/div/span/span')))
        post_button.click()

    def write_tweet(self):
        write_input = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/'
                                                      'div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/'
                                                      'div[1]/div/div/div/'
                                                      'div/div/div/div/div/div/div/label/'
                                                      'div[1]/div/div/div/div/div/div[2]/div/div/div/div')))
        write_input.send_keys(f"Hey Vodafone, my internet speed is awesome! Thank for giving me "
                              f"Download:{self.internet_speed.downl_speed} and Upload:{self.internet_speed.upl_speed}. "
                              f"You rock!")
        try:
            self.post_tweet_button()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.driver.quit()
