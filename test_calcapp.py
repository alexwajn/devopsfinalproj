from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pytest

def get_result(a, b):

    driver = webdriver.Firefox()
    driver.get("http://localhost:5000")
    
    time.sleep(2)
    
    elem = driver.find_element(By.NAME, "a")
    elem.send_keys(a)
    
    elem = driver.find_element(By.NAME, "b")
    elem.send_keys(b)
    
    elem = driver.find_element(By.ID, "subs")
    elem.click()
    
    elem.send_keys(Keys.RETURN)
    
    time.sleep(2)

    elem = driver.find_element(By.NAME, "result")
    result = elem.get_attribute('innerHTML')
    driver.close()
    return result

def test_res():
    assert "3087" in get_result("4321", "1234")

