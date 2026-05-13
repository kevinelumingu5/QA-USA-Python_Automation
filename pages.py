from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
import helpers

class UrbanRoutesPage:

    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')
    CALL_TAXI_LOCATOR = (By.XPATH, "//button[text()='Call a taxi']")
    SUPPORTIVE_BUTTON_LOCATOR = (By.XPATH, '//div[text()="Supportive"]')
    PHONE_NUMBER_BUTTON_LOCATOR = (By.CLASS_NAME, 'np-button')
    PHONE_NUMBER_INPUT_LOCATOR = (By.XPATH, '//*[@id="phone"]')
    SMS_CODE_INPUT_LOCATOR = (By.XPATH, '//*[@id="code"]')
    CONFIRM_BUTTON_LOCATOR = (By.XPATH, "//button[text()='Confirm']")
    PHONE_NUMBER_VALUE_LOCATOR = (By.XPATH, '//div[@class="np-text"]')

    PAYMENT_METHOD_BUTTON = (By.CLASS_NAME, "pp-text")
    ADD_CARD_BUTTON_LOCATOR = (By.CLASS_NAME, 'pp-plus-container')
    CARD_NUMBER_INPUT_LOCATOR = (By.XPATH, '//*[@id="number"]')
    CODE_INPUT_LOCATOR = (By.XPATH, '//input[@class="card-input" and @id="code"]')
    LINK_BUTTON_LOCATOR = (By.XPATH, '//button[text()="Link"]')
    X_CANCEL_CARD_BUTTON = (By.XPATH, '(//button[@class="close-button section-close"])[3]')
    CARD_NUMBER_VALUE_LOCATOR = (By.XPATH, '(//div[text()="Card"])[2]')

    MESSAGE_DRIVER_INPUT_LOCATOR = (By.XPATH, '//*[@id="comment"]')

    BLANKETS_AND_HANDKERCHIEFS_BUTTON_LOCATOR = (By.CSS_SELECTOR, '.slider.round')

    ICE_CREAM_PLUS_BUTTON_LOCATOR = (By.XPATH, '//div[@class="counter-plus"]')
    ICE_VALUE_LOCATOR = (By.XPATH, '//div[@class="counter-value"]')

    ENTER_BUTTON_LOCATOR = (By.XPATH, '//span[@class="smart-button-secondary"]')

    CAR_SEARCH_TEXT_LOCATOR = (By.XPATH, '//div[text()="Car search"]')
    OPTION_SWITCHES = (By.CLASS_NAME, 'switch')
    OPTION_SWITCHES_INPUTS = (By.CLASS_NAME, 'switch-input')

    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()

    def enter_locations(self, from_locator, to_locator,):
        self.driver.find_element(*self.FROM_LOCATOR).send_keys(from_locator)
        self.driver.find_element(*self.TO_LOCATOR).send_keys(to_locator)

    def get_from_location(self):
        return self.driver.find_element(*self.FROM_LOCATOR).get_attribute('value')


    def get_to_location(self):
        return self.driver.find_element(*self.TO_LOCATOR).get_attribute('value')

    def select_supportive(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.CALL_TAXI_LOCATOR)).click()
        self.driver.find_element(*self.CALL_TAXI_LOCATOR).click()
        self.driver.find_element(*self.SUPPORTIVE_BUTTON_LOCATOR).click()

    def get_supportive(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.CALL_TAXI_LOCATOR))
        return self.driver.find_element(*self.SUPPORTIVE_BUTTON_LOCATOR).text

    def enter_phone_number(self, phone_number):
        self.driver.find_element(*self.PHONE_NUMBER_BUTTON_LOCATOR).click()
        self.driver.find_element(*self.PHONE_NUMBER_INPUT_LOCATOR).send_keys(phone_number)
        self.driver.find_element(*self.PHONE_NUMBER_INPUT_LOCATOR).send_keys(Keys.ENTER)
        self.driver.find_element(*self.SMS_CODE_INPUT_LOCATOR).send_keys(helpers.retrieve_phone_code(self.driver))
        self.driver.find_element(*self.SMS_CODE_INPUT_LOCATOR).send_keys(Keys.ENTER)

    def get_phone_number(self):
        return self.driver.find_element(*self.PHONE_NUMBER_VALUE_LOCATOR).text

    def enter_payment_method(self, number_input, code_input):
        self.driver.find_element(*self.PAYMENT_METHOD_BUTTON).click()
        self.driver.find_element(*self.ADD_CARD_BUTTON_LOCATOR).click()
        self.driver.find_element(*self.CARD_NUMBER_INPUT_LOCATOR).send_keys(number_input)
        self.driver.find_element(*self.CODE_INPUT_LOCATOR).send_keys(code_input)
        self.driver.find_element(*self.CARD_NUMBER_INPUT_LOCATOR).click()
        time.sleep(2)
        self.driver.find_element(*self.LINK_BUTTON_LOCATOR).click()
        time.sleep(2)
        self.driver.find_element(*self.X_CANCEL_CARD_BUTTON).click()

    def get_card_attribute(self):
        return self.driver.find_element(*self.CARD_NUMBER_VALUE_LOCATOR).text


    def enter_message(self, message):
        self.driver.find_element(*self.MESSAGE_DRIVER_INPUT_LOCATOR).send_keys(message)

    def get_message_attribute(self):
        return self.driver.find_element(*self.MESSAGE_DRIVER_INPUT_LOCATOR).get_property('value')


    def activate_blankets_and_handkerchefs(self):
        self.driver.find_element(*self.BLANKETS_AND_HANDKERCHIEFS_BUTTON_LOCATOR).click()

    def get_handkerchefs(self):
        return self.driver.find_element(*self.BLANKETS_AND_HANDKERCHIEFS_BUTTON_LOCATOR).text

    def add_ice_cream(self):
        self.driver.find_element(*self.ICE_CREAM_PLUS_BUTTON_LOCATOR).click()
    def get_ice_cream(self):
        return self.driver.find_element(*self.ICE_VALUE_LOCATOR).text

    def order(self):
        self.driver.find_element(*self.ENTER_BUTTON_LOCATOR).click()

    def car_text(self):
        return self.driver.find_element(*self.CAR_SEARCH_TEXT_LOCATOR).text

    def get_blanket_and_handkerchiefs_option_checked(self):
        switches = self.driver.find_elements(*self.OPTION_SWITCHES_INPUTS)
        return switches[0].get_property('checked')