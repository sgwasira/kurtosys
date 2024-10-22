import time

import allure
import pytest

from Pages.homePage import HomePage
from Pages.whitePapersPages import WhitePapersPage
from Utils.readProperties_UrlDetails import ReadUrlConfig


class Test_01_contactForm:
    kurtosysURL = ReadUrlConfig().getKurtosysURL()

    @pytest.mark.contactForm
    def test_01Test(self, setup):
        self.driver = setup
        self.driver.get(self.kurtosysURL)
        self.driver.maximize_window()
        self.home = HomePage(self.driver)
        self.home.scrollDownToResource()
        time.sleep(3)
        self.home.clickWhitePapersAndeBooksLink()
        time.sleep(2)

        self.whitePapers = WhitePapersPage(self.driver)
        time.sleep(2)

        self.whitePapers.verifyWhitePapersTitleText()
        time.sleep(7)
        self.whitePapers.clickUCITSWhitePaper()
