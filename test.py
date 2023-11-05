from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Load up browser and set window to full screen
driver = webdriver.Chrome()
driver.maximize_window()

# Load webpage
driver.get('https://en.wikipedia.org/wiki/Main_Page')

# Find for Search textbox, enter text, and enter return
time.sleep(2)
search = driver.find_element(By.ID, "searchInput")
search.send_keys("sneed")
time.sleep(1)
search.send_keys(Keys.RETURN)

# Search for link on webpage
time.sleep(2)
findPage = driver.find_element(By.LINK_TEXT, "Chris Sneed")
findPage.click()

# Perform direct search query
time.sleep(5)
driver.get('https://www.youtube.com/results?search_query={}'.format(str("Jordan Peterson Gives a Lecture on SNEED")))

# Wait for items to become available
wait = WebDriverWait(driver, 3)
presence = EC.presence_of_element_located
visible = EC.visibility_of_element_located

# Wait for first item to become available and open link
wait.until(visible((By.ID, "video-title")))
driver.find_element(By.ID, "video-title").click()

# Ensures webpage doesn't close on running of program
while(True):
    pass
