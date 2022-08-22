from lib2to3.pgen2 import driver
from time import time
from unicodedata import name
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import unittest
import softest
driver = webdriver.Edge(executable_path='C:\Windows\msedgedriver.exe')

driver.get('https://rahulshettyacademy.com/angularpractice/')
driver.maximize_window()
name = driver.find_element(By.NAME, 'name').send_keys('Jameson Susanto')
email = driver.find_element(By.NAME, 'email').send_keys('jamesonsusanto0000@gmail.com')
password = driver.find_element(By.ID, 'exampleInputPassword1').send_keys('123456789')
CheckBox = driver.find_element(By.ID, 'exampleCheck1').click()
dropdown = driver.find_element(By.ID,'exampleFormControlSelect1')
dd = Select(dropdown)
dd.select_by_visible_text("Female")
dropdown2 = driver.find_element(By.ID,'inlineRadio1').click()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)
bday= driver.find_element(By.NAME,'bday').send_keys('09/03/2000')
time.sleep(3)
submit = driver.find_element(By.XPATH,'/html/body/app-root/form-comp/div/form/input').click()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)
class Test(unittest.TestCase):
    def testURL(self):
        urlcheck = driver.current_url
        self.assertEqual("https://rahulshettyacademy.com/angularpractice/", urlcheck)
    def testEmail(self):
        emailcheck = driver.find_element(By.NAME, 'name')
        self.assertNotEqual("Jameson Susanto",emailcheck)
        

if __name__== "__main__":
 unittest.main()


driver.quit()