from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.common.keys import Keys
"""
Initialize the Chrome driver
"""
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
sleep(3)
driver.maximize_window()

"""
Open the main webpage
"""
driver.get("https://www.cowin.gov.in/")
sleep(3)
"""
Find and click on the FAQs link
"""
faqs_link = driver.find_element(By.XPATH, value= "//*[@id='navbar']/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[4]/a")
faqs_link.send_keys(Keys.CONTROL + Keys.RETURN)
sleep(3)
"""
Find and click on the Partners link
"""
faqs_link = driver.find_element(By.XPATH, value= "//*[@id='navbar']/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[5]/a")
faqs_link.send_keys(Keys.CONTROL + Keys.RETURN)
sleep(3)
"""
Switch to the newly opened windows
"""
windows = driver.window_handles
driver.switch_to.window(windows[1])
faqs_title = driver.title
print("FAQs Window Title:", faqs_title)
sleep(3)
driver.close()

driver.switch_to.window(windows[2])
partners_title = driver.title
print("Partners Window Title:", partners_title)
sleep(3)
driver.close()

sleep(3)
driver.switch_to.window(windows[0])

"""
Close the driver
"""
driver.quit()

"""
Output- 
FAQs Window Title: CoWIN
Partners Window Title: CoWIN
"""




