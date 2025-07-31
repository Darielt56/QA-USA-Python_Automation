
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import retrieve_phone_code
from selenium.webdriver import Keys
import time


class UrbanRoutesPage:
    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')
    TAXI_BUTTON_LOCATOR = (By.XPATH, '//button[@type="button" and @class="button round"]')
    SUPPORTIVE_PLAN_LOCATOR = (By.XPATH, '//div[@class="tcard" and contains(.,"Supportive")]')
    VERIFY_SUPPORTIVE_PLAN_LOCATOR = (By.XPATH, '//div[@class="tcard active"]')
    PHONE_NUMBER_LOCATOR = (By.XPATH, "//div[@class='np-button']")
    PHONE_NUMBER_INPUT_LOCATOR = (By.ID, 'phone')
    NEXT_BUTTON_LOCATOR = (By.XPATH, "//button[@type='submit' and @class ='button full']")
    PHONE_CLOSE_BUTTON_LOCATOR = (By.XPATH, "//button[@class='close-button section-close']")
    CODE_LOCATOR = (By.XPATH, "//input[@id='code' and @class='input']")
    CONFIRM_BUTTON_LOCATOR = (By.XPATH, '//button[@type="submit" and contains(.,"Confirm")]')
    PAYMENT_METHOD_LOCATOR = (By.XPATH, '//div[@class="pp-button filled"]//div[@class="pp-text"]')
    ADD_CARD_LOCATOR = (By.XPATH, "//div[@class='pp-title' and text()='Add card']")
    CARD_NUMBER_INPUT_LOCATOR = (By.XPATH, '//div[@class="card-number-input"]')
    CARD_CODE_LOCATOR = (By.XPATH, '//div[@class="card-code-input"]')
    LINK_ACTIVE_LOCATOR = (By.XPATH, '//div[@class="overlay"]')
    LINK_LOCATOR = (By.XPATH, "//button[@class='button full' and text()='Link']")
    CLOSE_BUTTON_LOCATOR = (By.XPATH, "//button[@class='close-button section-close']")
    VERIFY_CARD_LOCATOR = (By.XPATH, '//div[@class="pp-value-text" and text()="Card"]')
    COMMENT_LOCATOR = (By.XPATH, "//input[@id='comment' and @class='input']")

    BLANKET_AND_HANDKERCHIEFS_LOCATOR = (By.XPATH, '//input[@type="checkbox" and @class="switch-input"]')
    BLANKET_AND_HANDKERCHIEFS_SWITCH_LOCATOR = (By.CLASS_NAME, 'switch')
    BLANKET_AND_HANDKERCHIEFS_SWITCH_INPUT_LOCATOR = (By.CLASS_NAME, 'switch-input')

    ICE_CREAM_LOCATOR = (By.XPATH, '//div[@class="counter"]//div[@class="counter-plus"]')
    ICE_CREAM_VALUE_LOCATOR = (By.XPATH, '//div[@class="counter"]//div[@class="counter-value"]')

    ORDER_BUTTON_LOCATOR = (By.XPATH, "//button[@class='smart-button']")
    CAR_SEARCH_MODAL_LOCATOR = (By.XPATH, '//div[@class="order-header-title"]')

    def __init__(self, driver):
        self.driver = driver

    def enter_from_location(self, from_text):
        self.driver.find_element(*self.FROM_LOCATOR).send_keys(from_text)
        return self.driver.find_element(*self.FROM_LOCATOR).get_attribute("value")

    def enter_to_location(self, to_text):
        self.driver.find_element(*self.TO_LOCATOR).send_keys(to_text)
        return self.driver.find_element(*self.TO_LOCATOR).get_attribute("value")

    def click_taxi_button(self):
        self.driver.find_element(*self.TAXI_BUTTON_LOCATOR).click()

    def click_supporting_plan_button(self):
        self.driver.find_element(*self.SUPPORTIVE_PLAN_LOCATOR).click()

    def verify_supporting_plan(self):
        return self.driver.find_element(*self.VERIFY_SUPPORTIVE_PLAN_LOCATOR).get_attribute("class")

    def click_phone_number(self):
        self.driver.find_element(*self.PHONE_NUMBER_LOCATOR).click()

    def enter_phone_number(self, phone_number):
        element = self.driver.find_element(*self.PHONE_NUMBER_INPUT_LOCATOR)
        element.send_keys(phone_number)
        return element.get_attribute("value")

    def click_next_button(self):
        self.driver.find_element(*self.NEXT_BUTTON_LOCATOR).click()

    def enter_code(self):
        code = retrieve_phone_code(self.driver)
        self.driver.find_element(*self.CODE_LOCATOR).send_keys(code)

    def click_confirm_button(self):
        self.driver.find_element(*self.CONFIRM_BUTTON_LOCATOR).click()

    def click_payment_method(self):
        self.driver.find_element(*self.PAYMENT_METHOD_LOCATOR).click()

    def click_add_card(self):
        self.driver.find_element(*self.ADD_CARD_LOCATOR).click()

    def enter_card_number(self, card_number):
        card_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CARD_NUMBER_INPUT_LOCATOR))
        card_input.send_keys(card_number)

    def enter_card_code(self, code):
        self.driver.find_element(*self.CODE_LOCATOR).send_keys(code)

    def click_link_active(self):
        self.driver.find_element(*self.LINK_ACTIVE_LOCATOR).click()

    def click_link_button(self):
        self.driver.find_element(*self.LINK_LOCATOR).click()

    def click_close_button(self):
        self.driver.find_element(*self.CLOSE_BUTTON_LOCATOR).click()

    def verify_card(self):
        self.driver.find_element(*self.VERIFY_CARD_LOCATOR).text()

    def enter_comment_for_driver(self, message):
        self.driver.find_element(*self.COMMENT_LOCATOR).send_keys(message)

    def get_message_for_driver(self):
        return self.driver.find_element(*self.COMMENT_LOCATOR).get_attribute("value")

    def click_blanket_and_handkerchiefs_option(self):
        switches = self.driver.find_elements(*self.BLANKET_AND_HANDKERCHIEFS_SWITCH_LOCATOR)
        switches[0].click()
        self.get_blanket_and_handkerchiefs_option_checked()

    def get_blanket_and_handkerchiefs_option_checked(self):
        switches = self.driver.find_elements(*self.BLANKET_AND_HANDKERCHIEFS_SWITCH_INPUT_LOCATOR)
        return switches[0].get_property('checked')

    def click_blankets_and_handkerchiefs(self):
        self.driver.find_element(*self.BLANKET_AND_HANDKERCHIEFS_LOCATOR).click()

    def verify_blankets_and_handkerchiefs(self):
        return self.driver.find_element(*self.BLANKET_AND_HANDKERCHIEFS_LOCATOR).get_property("checked")

    def click_ice_cream(self):
        for ice_cream in range(2):
            self.driver.find_element(*self.ICE_CREAM_LOCATOR).click()

    def get_ice_cream(self):
        return self.driver.find_element(*self.ICE_CREAM_VALUE_LOCATOR).text

    def click_order_button(self):
        self.driver.find_element(*self.ORDER_BUTTON_LOCATOR).click()

    def verify_car_search_modal(self):
        modal = self.driver.find_element(*self.CAR_SEARCH_MODAL_LOCATOR)
        return modal.is_displayed()

    def enter_locations(self, from_text, to_text):
        self.enter_from_location(from_text)
        self.enter_to_location(to_text)

    def get_locations_value(self):
        real_from = self.driver.find_element(*self.FROM_LOCATOR).get_attribute("value")
        real_to = self.driver.find_element(*self.TO_LOCATOR).get_attribute("value")
        return real_from, real_to

    def get_phone_number_value(self):
        phone_number_value = self.driver.find_element(*self.PHONE_NUMBER_INPUT_LOCATOR).get_attribute("value")
        return phone_number_value

    def set_card(self, card_number, code):
        self.enter_card_number(card_number)
        self.enter_card_code(code)
        self.click_link_active()
        self.click_link_button()
        self.click_close_button()
