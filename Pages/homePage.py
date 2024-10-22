from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    resource_element_xpath = "//span[@class='elementor-heading-title elementor-size-default'][contains(.,'Resources')]"
    whitePapersAndeBooks_element_xpath = "(//span[@class='elementor-icon-list-text'][contains(.,'White Papers & eBooks')])[3]"

    def __init__(self, driver):
        self.driver = driver

    def scrollDownToResource(self):
        wait = WebDriverWait(self.driver, 10)
        resource_element = wait.until(EC.visibility_of_element_located((By.XPATH, self.resource_element_xpath)))
        self.driver.execute_script("arguments[0].scrollIntoView();", resource_element)

    def clickWhitePapersAndeBooksLink(self):
        wait = WebDriverWait(self.driver, 10)
        whitePapersAndeBooks_element = wait.until(EC.element_to_be_clickable((By.XPATH, self.whitePapersAndeBooks_element_xpath)))
        whitePapersAndeBooks_element.click()
