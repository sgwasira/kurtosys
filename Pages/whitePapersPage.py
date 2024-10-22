from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WhitePapersPage:
    whitePapersTitle_element_xpath = "//h2[@class='elementor-heading-title elementor-size-default'][contains(.,'White Papers')]"
    UCITSWhitePaper_element_xpath = "//a[contains(.,'Institutional reporting survey')]"

    def __init__(self, driver):
        self.driver = driver

    def verifyWhitePapersTitleText(self):
        wait = WebDriverWait(self.driver, 10)
        whitePapersTitle_element = wait.until(EC.visibility_of_element_located((By.XPATH, self.whitePapersTitle_element_xpath)))
        whitePapersTitle_element.is_displayed()

    def clickUCITSWhitePaper(self):
        wait = WebDriverWait(self.driver, 10)
        UCITSWhitePaper_element = wait.until(EC.element_to_be_clickable((By.XPATH, self.UCITSWhitePaper_element_xpath)))
        UCITSWhitePaper_element.click()

