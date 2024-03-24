from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from time import sleep
import requests
import os

"""
To download Monthly progress report
"""
url = "https://labour.gov.in/sites/default/files/mpr_january_2024.pdf"

response = requests.get(url)

if response.status_code == 200:
    f = open("monthlyProgressReport.pdf", "wb")
    f.write(response.content)
    print("Successfully downloaded PDF")
    f.close()
else:
    print("Error")

sleep(5)

"""
Create a folder to store the downloaded images
"""
folder_name = "photo_gallery"
os.makedirs(folder_name, exist_ok=True)


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


driver.get("https://labour.gov.in/")

"""
Click on the "Media" menu
"""
media_menu = driver.find_element(By.XPATH, value="//*[@id='nav']/li[10]/a")
media_menu.click()


sleep(3)
"""
Click on Photo Gallery
"""
photo_gallery_submenu = driver.find_element(By.XPATH, value="//*[@id='block-block-88']/ul/li[2]/strong/a")
photo_gallery_submenu.click()


sleep(3)
image_urls= [
    "https://labour.gov.in/sites/default/files/5_9_0.jpg",
    "https://labour.gov.in/sites/default/files/4_12_0.jpg",
    "https://labour.gov.in/sites/default/files/3_17_0.jpg",
    "https://labour.gov.in/sites/default/files/2_13_0.jpg",
    "https://labour.gov.in/sites/default/files/1_28_0.jpg",
    "https://labour.gov.in/sites/default/files/58_0.jpg",
    "https://labour.gov.in/sites/default/files/57_0.jpg",
    "https://labour.gov.in/sites/default/files/56_0.jpg",
    "https://labour.gov.in/sites/default/files/55_0.jpg",
    "https://labour.gov.in/sites/default/files/54_0.jpg"

]


"""
Download 10 images
"""
for i, url in enumerate(image_urls, 1):
    response = requests.get(url)

    if response.status_code == 200:

        with open(os.path.join(folder_name,f"image_{i}.jpg"), "wb") as f:
            f.write(response.content)
        print(f"Image {i} downloaded successfully.")
    else:
        print("Error")

"""
Quit the WebDriver
"""
driver.quit()


"""
Output-
Successfully downloaded PDF
Image 1 downloaded successfully.
Image 2 downloaded successfully.
Image 3 downloaded successfully.
Image 4 downloaded successfully.
Image 5 downloaded successfully.
Image 6 downloaded successfully.
Image 7 downloaded successfully.
Image 8 downloaded successfully.
Image 9 downloaded successfully.
Image 10 downloaded successfully.
"""


