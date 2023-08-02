from selenium.webdriver.common.by import By


class Test_credkart():

    def test_Credkart_login_02(self, setup,get_data_for_login):
        self.driver = setup
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()
        self.driver.find_element(By.XPATH, "//input[@id='email']").send_keys(get_data_for_login[0])
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys(get_data_for_login[1])
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        try:
            self.driver.find_element(By.XPATH, "//h2[normalize-space()='CredKart']")
            print('Login case is passed')
            self.driver.save_screenshot(f".\\screenshots\\{get_data_for_login[0]}_{get_data_for_login[1]}login_pass_02.PNG")
            self.driver.close()
            assert True
        except:
            print('Login case is failed')
            self.driver.save_screenshot(f".\\screenshots\\{get_data_for_login[0]}_{get_data_for_login[1]}login_fail_02.PNG")
            self.driver.close()
            assert False