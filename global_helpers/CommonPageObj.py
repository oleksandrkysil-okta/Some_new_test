import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from global_helpers.constants import TIMEOUTS


class CommonPageObj():
    # TODO create retry decorator and remove all waiter loops
    def __init__(self, driver):
        self.driver = driver,
        # TODO implement locators
   #     self.locators =

    def open(self, url):
        "Navigates to given URL"
        self.driver.get(url)

    def wait_page_opened(self, timeout=TIMEOUTS['nano']):
        "Wait for certain time for page to be loaded"
        for attempt in range(10):
            try:
                is_page_loaded = self.driver.execute_script("return document.readyState;")
                assert is_page_loaded
            except Exception as ex:
                time.sleep(timeout)
                if attempt == 10:
                    raise ex(f'{ex.__class__.__name__}, Page wasn`t opened for {timeout} period')

    def is_page_opened(self, expected_url):
        "Compare given URL with actual"
        actual_page = self.driver.current_url
        assert actual_page == expected_url, f'Current page: {actual_page} didn`t match to expected {expected_url}'

    def wait_for_element_present(self, element_locator, timeout=TIMEOUTS['nano']):
        "Wait for element to appear"
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(element_locator))
        except Exception as ex:
           raise ex(f'Element didn`t appear after 5 seconds. Received {ex.__class__.__name__} error')

        return element

    def is_element_visible(self, element_locator):
        "Verifies if element displayed"
        element = self.driver.find_element(element_locator)
        assert element.is_displayed(), f"Element with locator {element_locator} is not displayed"

    def wait_for_element_and_click(self, element_locator):
        "Wait for element to be clicked"
        try:
            element = WebDriverWait(self.driver, TIMEOUTS['medium']).until(
                EC.element_to_be_clickable(element_locator))
        except Exception as ex:
               raise ex(f'{ex.__class__.__name__} received. Element is not clickable or not present')

        element.click()

    def wait_element_disappear(self, element_locator):
        "Wait for element to disapear"
        try:
            is_element_visible = WebDriverWait(self.driver, TIMEOUTS['medium']).until(
                EC.invisibility_of_element_located(element_locator))
        except Exception as ex:
            raise ex(f'{ex.__class__.__name__} received. Element didn`t disappear for expected time')

        return is_element_visible

    def scroll_2_element(self, element):
        "Scrolls to given webElement"
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()