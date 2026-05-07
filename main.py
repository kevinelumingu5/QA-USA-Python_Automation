import data
import helpers
from selenium import webdriver
from pages import UrbanRoutesPage
import time

kevv = "https://cnt-f3dccad3-112b-438e-8351-d9ee6156b4db.containerhub.tripleten-services.com"

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
        self.driver.get(kevv)
        urban_test = UrbanRoutesPage(self.driver)
        urban_test.enter_locations("east", "1300")
        time.sleep(4)
        print("function created for test_set_route")
        pass

    def test_select_plan(self):
        self.driver.get(kevv)
        urban_test = UrbanRoutesPage(self.driver)
        urban_test.enter_locations("east", "1300")
        time.sleep(2)
        urban_test.select_supportive()
        time.sleep(2)
        print("function created for test_select_plan")
        pass

    def test_fill_phone_number(self):
        self.driver.get(kevv)
        urban_test = UrbanRoutesPage(self.driver)
        urban_test.enter_locations("east", "1300")
        time.sleep(2)
        urban_test.select_supportive()
        time.sleep(2)
        urban_test.enter_phone_number("+1 1312121212")
        time.sleep(6)
        print("function created for test_fill_phone_number")
        pass

    def test_fill_card(self):
        self.driver.get(kevv)
        urban_test = UrbanRoutesPage(self.driver)
        urban_test.enter_locations("east", "1300")
        time.sleep(2)
        urban_test.select_supportive()
        time.sleep(2)
        urban_test.enter_phone_number("+1 1312121212")
        time.sleep(6)
        urban_test.enter_payment_method("123 123 123", "12")
        time.sleep(2)
        print("function created for test_fill_card")
        pass

    def test_comment_for_driver(self):
        self.driver.get(kevv)
        urban_test = UrbanRoutesPage(self.driver)
        urban_test.enter_locations("east", "1300")
        time.sleep(2)
        urban_test.select_supportive()
        time.sleep(2)
        urban_test.enter_phone_number("+1 1312121212")
        time.sleep(6)
        urban_test.enter_payment_method("123 123 123", "12")
        time.sleep(2)
        urban_test.enter_message('Stop at the juice bar, please')
        print("function created for test_comment_for_driver")
        pass

    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(kevv)
        urban_test = UrbanRoutesPage(self.driver)
        urban_test.enter_locations("east", "1300")
        time.sleep(2)
        urban_test.select_supportive()
        time.sleep(2)
        urban_test.enter_phone_number("+1 1312121212")
        time.sleep(6)
        urban_test.enter_payment_method("123 123 123", "12")
        time.sleep(2)
        urban_test.enter_message('Stop at the juice bar, please')
        time.sleep(2)
        urban_test.activate_blankets_and_handkerchefs()
        time.sleep(2)
        print("function created for test_order_blanket_and_handkerchiefs")
        pass

    def test_order_2_ice_creams(self):
        self.driver.get(kevv)
        urban_test = UrbanRoutesPage(self.driver)
        urban_test.enter_locations("east", "1300")
        time.sleep(2)
        urban_test.select_supportive()
        time.sleep(2)
        urban_test.enter_phone_number("+1 1312121212")
        time.sleep(6)
        urban_test.enter_payment_method("123 123 123", "12")
        time.sleep(2)
        urban_test.enter_message('Stop at the juice bar, please')
        time.sleep(2)
        urban_test.activate_blankets_and_handkerchefs()
        time.sleep(2)
        urban_test.add_ice_cream()
        time.sleep(2)
        for i in range(2):
            urban_test.add_ice_cream()
            time.sleep(2)
            print("function created for test_order_2_ice_creams")
            pass

    def test_car_search_model_appears(self):
        self.driver.get(kevv)
        urban_test = UrbanRoutesPage(self.driver)
        urban_test.enter_locations("east", "1300")
        time.sleep(2)
        urban_test.select_supportive()
        time.sleep(2)
        urban_test.enter_phone_number("+1 1312121212")
        time.sleep(2)
        urban_test.enter_payment_method("123 123 123", "12")
        time.sleep(2)
        urban_test.enter_message('Stop at the juice bar, please')
        time.sleep(2)
        urban_test.activate_blankets_and_handkerchefs()
        time.sleep(2)
        urban_test.add_ice_cream()
        time.sleep(2)
        for i in range(2):
            urban_test.add_ice_cream()
            time.sleep(2)
        urban_test.order()
        time.sleep(2)
        expected = urban_test.car_text()
        actual = "Car search"
        assert actual in expected, f"Expected '{actual}', but got '{expected}'"
        print("function created for test_car_search_model_appears")
        pass


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()