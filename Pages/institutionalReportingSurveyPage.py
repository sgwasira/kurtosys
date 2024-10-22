from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class institutionalReportingSurveyPage:
    firstName_element_xpath = "//input[contains(@placeholder,'First name*')]"
    lastName_element_xpath = "//input[contains(@placeholder,'Last name*')]"
    email_element_xpath = "//input[contains(@placeholder,'Last name*')]"
    subscribeButton_element_xpath = "//span[@class='elementor-button-text'][contains(.,'Subscribe')]"

    def __init__(self, driver):
        self.driver = driver

    def enterFirstName(self, firstName):
        wait = WebDriverWait(self.driver, 10)
        firstName_element = wait.until(EC.element_to_be_clickable((By.XPATH, self.firstName_element_xpath)))
        firstName_element.send_keys(firstName)

    def enterLastName(self, lastName):
        wait = WebDriverWait(self.driver, 10)
        lastName_element = wait.until(EC.element_to_be_clickable((By.XPATH, self.lastName_element_xpath)))
        lastName_element.send_keys(lastName)

    def enterEmail(self, email):
        wait = WebDriverWait(self.driver, 10)
        email_element = wait.until(EC.element_to_be_clickable((By.XPATH, self.email_element_xpath)))
        email_element.send_keys(email)

    def clickSubscribeButton(self):
        wait = WebDriverWait(self.driver, 10)
        subscribeButton_element = wait.until(EC.element_to_be_clickable((By.XPATH, self.subscribeButton_element_xpath)))
        subscribeButton_element.click()


