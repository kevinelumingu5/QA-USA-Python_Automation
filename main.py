import data
import helpers
from selenium import webdriver

import pages
from pages import UrbanRoutesPage
import time



class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")

        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()


    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_test = UrbanRoutesPage(self.driver)
        urban_test.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        time.sleep(4)
        assert urban_test.get_from_locattion() == data.ADDRESS_FROM
        assert urban_test.get_to_locattion() == data.ADDRESS_TO


    def test_select_plan(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_test = UrbanRoutesPage(self.driver)
        urban_test.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        time.sleep(2)
        urban_test.select_supportive()
        time.sleep(2)
        urban_test.get_supportive() == "Suppotive"

    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_test = UrbanRoutesPage(self.driver)
        urban_test.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        time.sleep(2)
        urban_test.select_supportive()
        time.sleep(2)
        urban_test.enter_phone_number(data.PHONE_NUMBER)
        time.sleep(6)
        assert urban_test.get_phone_number() == data.PHONE_NUMBER

    def test_fill_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_test = UrbanRoutesPage(self.driver)
        urban_test.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        time.sleep(2)
        urban_test.select_supportive()
        time.sleep(2)
        urban_test.enter_phone_number(data.PHONE_NUMBER)
        time.sleep(6)
        urban_test.enter_payment_method(data.CARD_NUMBER, data.CARD_NUMBER)
        time.sleep(2)
        assert urban_test.get_card_attribute() == data.CARD_NUMBER

    def test_comment_for_driver(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_test = UrbanRoutesPage(self.driver)
        urban_test.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        time.sleep(2)
        urban_test.select_supportive()
        time.sleep(2)
        urban_test.enter_phone_number(data.PHONE_NUMBER)
        time.sleep(6)
        urban_test.enter_payment_method(data.CARD_NUMBER, data.CARD_CODE)
        time.sleep(2)
        urban_test.enter_message(data.MESSAGE_FOR_DRIVER)
        assert urban_test.get_message_attribute() == data.MESSAGE_FOR_DRIVER

    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_test = UrbanRoutesPage(self.driver)
        urban_test.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        time.sleep(2)
        urban_test.select_supportive()
        time.sleep(2)
        urban_test.enter_phone_number(data.PHONE_NUMBER)
        time.sleep(6)
        urban_test.enter_payment_method(data.CARD_NUMBER, data.CARD_CODE)
        time.sleep(2)
        urban_test.enter_message(data.MESSAGE_FOR_DRIVER)
        time.sleep(2)
        urban_test.activate_blankets_and_handkerchefs()
        time.sleep(2)
        assert urban_test.get_blanket_and_handkerchiefs_option_checked()

    def test_order_2_ice_creams(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_test = UrbanRoutesPage(self.driver)
        urban_test.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        time.sleep(2)
        urban_test.select_supportive()
        time.sleep(2)
        urban_test.enter_phone_number(data.PHONE_NUMBER)
        time.sleep(6)
        urban_test.enter_payment_method(data.CARD_NUMBER, data.CARD_CODE)
        time.sleep(2)
        urban_test.enter_message(data.MESSAGE_FOR_DRIVER)
        time.sleep(2)
        urban_test.activate_blankets_and_handkerchefs()
        time.sleep(2)
        urban_test.add_ice_cream()
        time.sleep(2)
        for i in range(2):
            urban_test.add_ice_cream()
            time.sleep(2)
            pass
        assert urban_test.get_ice_cream() == "2"

    def test_car_search_model_appears(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_test = UrbanRoutesPage(self.driver)
        urban_test.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        time.sleep(2)
        urban_test.select_supportive()
        time.sleep(2)
        urban_test.enter_phone_number(data.PHONE_NUMBER)
        time.sleep(2)
        urban_test.enter_payment_method(data.CARD_NUMBER, data.CARD_CODE)
        time.sleep(2)
        urban_test.enter_message(data.MESSAGE_FOR_DRIVER)
        time.sleep(2)
        urban_test.activate_blankets_and_handkerchefs()
        time.sleep(2)
        urban_test.add_ice_cream()
        time.sleep(2)
        urban_test.order()
        time.sleep(2)
        expected = urban_test.car_text()
        actual = "Car search"
        assert actual in expected, f"Expected '{actual}', but got '{expected}'"


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()