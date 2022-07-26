# import required modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

options = Options()
options.add_argument("window-size=1200x600")
driver = webdriver.Edge(r'C:\Users\SARTHAK\OneDrive\Documents\edgedriver_win64\msedgedriver.exe', options=options)
driver.get("https://youtube.com")

try:
    searchBox = driver.find_element(by=By.XPATH, value='/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input')
    print("Runnning Successfluuy")
    driver.implicitly_wait(5)
    searchBox.send_keys("Carryminati")
    button = driver.find_element(by=By.XPATH, value='/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/button')
    button.click()
except Exception as e:
    print(e)

