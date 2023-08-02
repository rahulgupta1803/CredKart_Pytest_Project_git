import time

from selenium.webdriver.common.by import By


class Test_shopclues():

    def test_shopclues_login01(self,comm_file,shopclue_login_data):
        self.driver = comm_file
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Sign In']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[3]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Continue with Facebook']").click()
        self.driver.find_element(By.XPATH, "//input[@id='email']").send_keys(shopclue_login_data[0])
        self.driver.find_element(By.XPATH, "//input[@id='pass']").send_keys(shopclue_login_data[1])
        self.driver.find_element(By.XPATH, "//button[@id='loginbutton']").click()
        try:
            time.sleep(10)
            self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[3]/div[1]/button[1]").click()
            self.driver.find_element(By.XPATH, "//a[normalize-space()='Hi Rahul']")
            self.driver.find_element(By.XPATH,"//div[@class='hoverContent sc_actLinks']//a[contains(text(),'Rahul')]")
            self.driver.save_screenshot(f".//screenshots//{shopclue_login_data[0]}_{shopclue_login_data[1]} shopclues_login_pass01.PNG")
            print("shopclue login successfully")
            self.driver.close()
            assert True
        except:
            print("shopclue login is unsuccessfull")
            self.driver.save_screenshot(f".//screenshots//{shopclue_login_data[0]}_{shopclue_login_data[1]} shopcclues_login_fail01.PNG")
            self.driver.close()
            assert False
