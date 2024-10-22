import configparser

config = configparser.RawConfigParser
config.read("./Configurations/UrlDetails.ini")


class ReadUrlConfig():

    def getKurtosysURL(self):
        return config.get("URLS", "kurtosysURL")
