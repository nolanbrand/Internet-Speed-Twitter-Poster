from selenium import webdriver
from selenium.webdriver.common.by import By
import time

PROMISED_DOWN = 1000
PROMISED_UP = 5
SPEED_TEST_URL = "https://www.speedtest.net/"
TWITTER_URL = "https://x.com/i/flow/login"
TWITTER_USERNAME = "Your_Username"
TWITTER_PASSWORD = "Your_Password"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get(SPEED_TEST_URL)
        go_button = self.driver.find_element(By.XPATH, value='//*[text()="Go"]')
        go_button.click()
        time.sleep(38)
        measured_down = self.driver.find_element(By.XPATH,
                                                 value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/'
                                                       'div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        measured_up = self.driver.find_element(By.XPATH,
                                               value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/'
                                                     'div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.down = float(measured_down.text)
        self.up = float(measured_up.text)

    def tweet_at_provider(self):
        self.driver.get(TWITTER_URL)
        time.sleep(4)
        email_input = self.driver.find_element(By.CSS_SELECTOR, value='div label')
        email_input.click()
        email_input.send_keys(TWITTER_USERNAME)
        next_button = self.driver.find_element(By.XPATH, value='//*[text()="Next"]')
        next_button.click()
        time.sleep(3)
        password_input = self.driver.find_elements(By.CSS_SELECTOR, value='div label')
        password_input[1].send_keys(TWITTER_PASSWORD)
        log_in = self.driver.find_element(By.XPATH, value='//*[text()="Log in"]')
        log_in.click()
        time.sleep(3)
        tweet_draft = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/'
                                                               'div/div/div/div[3]/div/div[2]/div[1]/div/div/div/'
                                                               'div[2]/div[1]/div/div/div/div/div/div/div/div/div/'
                                                               'div/div/div[1]/div/div/div/div/div/div[2]/div/div/'
                                                               'div/div')

        if self.down < PROMISED_DOWN or self.up < PROMISED_UP:
            tweet_draft.click()
            tweet_draft.send_keys(
                f"Hey internet provider! Why is my internet speed {self.down} Mbps down and {self.up} "
                f"Mbps up when I pay for {PROMISED_DOWN} Mbps down and {PROMISED_UP} Mbps up?!")
        else:
            tweet_draft.send_keys("All good homies!")

        post = self.driver.find_element(By.XPATH, value='//*[text()="Post"]')
        post.click()
