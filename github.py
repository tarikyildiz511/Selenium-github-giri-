from githubuser import username,sifre
from selenium import webdriver
import time

class Github:
    def __init__(self,username,sifre):
        self.browser = webdriver.Chrome()
        self.username =username
        self.sifre = sifre
    def signIn(self,username,sifre):
        self.browser.get("https://github.com/login")
        time.sleep(2)
        username = self.browser.find_element_by_xpath("//*[@id='login_field']").send_keys(self.username)
        sifre = self.browser.find_element_by_xpath("//*[@id='password']").send_keys(self.sifre)

        time.sleep(1)
        self.browser.find_element_by_xpath("//*[@id='login']/div[4]/form/input[14]").click()
        
github = Github(username,sifre)
github.signIn(username,sifre)