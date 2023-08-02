from selenium import webdriver
from selenium.webdriver.common.by import By




class Test_CredKart_Login():


    def test_pageTilte01(self,setup):
        self.driver = setup
        if (self.driver.title =="CredKart"):
            self.driver.save_screenshot("D:\credence\CredKart_Pytest_Project\screenshots\page_title_pass01.PNG")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot("D:\credence\CredKart_Pytest_Project\screenshots\page_title_fail01.PNG")
            assert False

    def test_Credkart_login_02(self,setup):
        self.driver = setup
        self.driver.find_element(By.XPATH,"//a[normalize-space()='Login']").click()
        self.driver.find_element(By.XPATH, "//input[@id='email']").send_keys("Credencetest@test.com")
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Credence@123")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        try:
            self.driver.find_element(By.XPATH,"//h2[normalize-space()='CredKart']")
            print('Login case is passed')
            self.driver.save_screenshot("D:\credence\CredKart_Pytest_Project\screenshots\login_pass_02.PNG")
            self.driver.close()
            assert True
        except:
            print('Login case is failed')
            self.driver.save_screenshot("D:\credence\CredKart_Pytest_Project\screenshots\login_fail_02.PNG")
            self.driver.close()
            assert False






