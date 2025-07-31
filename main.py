import time

import data
import helpers
from selenium import webdriver
from data import URBAN_ROUTES_URL
from pages import UrbanRoutesPage


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):

        # do not modify - we need additional logging enabled in order to retrieve phone confirmation code
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(4)
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print(" Connected to the Urban Routes server")
        else:
            print("Cannot connect to thr Urban Routes server.Check the server is on and still running")

    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        from_value, to_value = routes_page.get_locations_value()
        assert from_value == data.ADDRESS_FROM
        assert to_value == data.ADDRESS_TO

    def test_select_plan(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_taxi_button()
        routes_page.click_supporting_plan_button()
        assert 'active' in routes_page.verify_supporting_plan()

    def test_fill_phone_number(self):
        self.driver.get(URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_taxi_button()
        routes_page.click_supporting_plan_button()
        routes_page.click_phone_number()
        routes_page.enter_phone_number(data.PHONE_NUMBER)
        routes_page.click_next_button()
        routes_page.enter_code()
        assert routes_page.get_phone_number_value() == data.PHONE_NUMBER

    def test_fill_card(self):
        self.driver.get(URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_taxi_button()
        routes_page.click_supporting_plan_button()
        time.sleep(2)
        routes_page.click_payment_method()
        routes_page.click_add_card()
        time.sleep(2)
        routes_page.set_card(data.CARD_NUMBER, data.CARD_CODE)
        routes_page.click_link_active()
        routes_page.click_link_button()
        routes_page.click_close_button()
        assert routes_page.verify_card() == 'Card'

    def test_comment_for_driver(self):
        self.driver.get(URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_taxi_button()
        routes_page.click_supporting_plan_button()
        routes_page.enter_comment_for_driver(data.MESSAGE_FOR_DRIVER)
        assert routes_page.get_message_for_driver() == data.MESSAGE_FOR_DRIVER

    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_taxi_button()
        routes_page.click_supporting_plan_button()
        routes_page.click_blanket_and_handkerchiefs_option()
        assert routes_page.get_blanket_and_handkerchiefs_option_checked() == True

    def test_order_2_ice_creams(self):
        self.driver.get(URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_taxi_button()
        routes_page.click_supporting_plan_button()
        routes_page.click_ice_cream()
        assert routes_page.get_ice_cream() == '2'

    def test_car_search_model_appears(self):
        self.driver.get(URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_taxi_button()
        routes_page.click_supporting_plan_button()
        routes_page.click_phone_number()
        routes_page.enter_phone_number(data.PHONE_NUMBER)
        routes_page.click_next_button()
        routes_page.enter_code()
        routes_page.click_confirm_button()
        routes_page.enter_comment_for_driver(data.MESSAGE_FOR_DRIVER)
        routes_page.click_order_button()
        assert routes_page.verify_car_search_modal()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
