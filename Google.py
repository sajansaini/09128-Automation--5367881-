from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.google.com/")


def search():
    search_test = driver.find_element(By.NAME, 'q')
    search_test.send_keys("Examination")
