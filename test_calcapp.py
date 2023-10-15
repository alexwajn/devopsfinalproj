from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://localhost:5000")
elem = driver.find_element(By.NAME, "a")
elem.send_keys("4321")

elem = driver.find_element(By.NAME, "b")
elem.send_keys("1234")

elem = driver.find_element(By.ID, "subs")
elem.click()

elem.send_keys(Keys.RETURN)

elem = driver.find_element(By.NAME, "result")
print(elem.get_attribute('innerHTML'))

driver.close()
