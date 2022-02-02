from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.youtube.com/")


def yousearch():
    search_test = driver.find_element(By.ID, 'search')
    search_test.send_keys("Github")
