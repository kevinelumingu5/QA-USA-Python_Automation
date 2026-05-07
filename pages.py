from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
import helpers


class UrbanRoutesPage:

    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')
    CALL_TAXI_LOCATOR = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[1]/div[3]/div[1]/button')
    SUPPORTIVE_BUTTON_LOCATOR = (By.XPATH, '//div[text()="Supportive"]')
    PHONE_NUMBER_BUTTON_LOCATOR = (By.CLASS_NAME, 'np-button')
    PHONE_NUMBER_INPUT_LOCATOR = (By.XPATH, '//*[@id="phone"]')
    SMS_CODE_INPUT_LOCATOR = (By.XPATH, '//*[@id="code"]')
    CONFIRM_BUTTON_LOCATOR = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[2]/form/div[2]/button[1]')
    X_CANCEL_BUTTON_LOCATOR = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[2]/button')

    PAYMENT_METHOD_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[2]/div[1]')
    ADD_CARD_BUTTON_LOCATOR = (By.CLASS_NAME, 'pp-plus-container')
    CARD_NUMBER_INPUT_LOCATOR = (By.XPATH, '//*[@id="number"]')
    CODE_INPUT_LOCATOR = (By.XPATH, '//div[@class="card-code-input"]//*[@id="code"]')
    LINK_BUTTON_LOCATOR = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/form/div[3]/button[1]')
    X_CANCEL_CARD_BUTTON = (By.XPATH, '//div[@class="payment-picker open"]//div[@class="section active"]//button[@class="close-button section-close"]')

    MESSAGE_DRIVER_INPUT_LOCATOR = (By.XPATH, '//*[@id="comment"]')

    BLANKETS_AND_HANDKERCHIEFS_BUTTON_LOCATOR = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/span')

    ICE_CREAM_PLUS_BUTTON_LOCATOR = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]')

    ENTER_BUTTON_LOCATOR = (By.XPATH, '//*[@id="root"]/div/div[3]/div[4]/button')

    CAR_SEARCH_TEXT_LOCATOR = (By.XPATH, '//*[@id="root"]/div/div[5]/div[2]/div[1]/div/div[1]')

    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()

    def enter_locations(self, to_locator, from_locator,):
        self.driver.find_element(*self.FROM_LOCATOR).send_keys(from_locator)
        self.driver.find_element(*self.TO_LOCATOR).send_keys(to_locator)

    def select_supportive(self):
        self.driver.find_element(*self.CALL_TAXI_LOCATOR).click()
        self.driver.find_element(*self.SUPPORTIVE_BUTTON_LOCATOR).click()

    def enter_phone_number(self, phone_number):
        self.driver.find_element(*self.PHONE_NUMBER_BUTTON_LOCATOR).click()
        self.driver.find_element(*self.PHONE_NUMBER_INPUT_LOCATOR).send_keys(phone_number)
        self.driver.find_element(*self.PHONE_NUMBER_INPUT_LOCATOR).send_keys(Keys.ENTER)
        self.driver.find_element(*self.SMS_CODE_INPUT_LOCATOR).send_keys(helpers.retrieve_phone_code(self.driver))
        self.driver.find_element(*self.SMS_CODE_INPUT_LOCATOR).send_keys(Keys.ENTER)

    def enter_payment_method(self, number_input, code_input):
        self.driver.find_element(*self.PAYMENT_METHOD_BUTTON).click()
        self.driver.find_element(*self.ADD_CARD_BUTTON_LOCATOR).click()
        self.driver.find_element(*self.CARD_NUMBER_INPUT_LOCATOR).send_keys(number_input)
        self.driver.find_element(*self.CODE_INPUT_LOCATOR).send_keys(code_input)
        self.driver.find_element(*self.CARD_NUMBER_INPUT_LOCATOR).click()
        self.driver.find_element(*self.LINK_BUTTON_LOCATOR).click()
        time.sleep(2)
        self.driver.find_element(*self.X_CANCEL_CARD_BUTTON).click()


    def enter_message(self, message):
        self.driver.find_element(*self.MESSAGE_DRIVER_INPUT_LOCATOR).send_keys(message)

    def activate_blankets_and_handkerchefs(self):
        self.driver.find_element(*self.BLANKETS_AND_HANDKERCHIEFS_BUTTON_LOCATOR).click()

    def add_ice_cream(self):
        self.driver.find_element(*self.ICE_CREAM_PLUS_BUTTON_LOCATOR).click()

    def order(self):
        self.driver.find_element(*self.ENTER_BUTTON_LOCATOR).click()

    def car_text(self):
        return self.driver.find_element(*self.CAR_SEARCH_TEXT_LOCATOR).text
