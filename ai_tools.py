from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
import time
import random 
from bs4 import BeautifulSoup
import pandas as pd

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

url = 'https://www.futuretools.io/?pricing-model=free'

# Open the URL
driver.get(url)
time.sleep(5)

# Scroll to the bottom of the page
for i in range(2):
    page = driver.find_element(By.TAG_NAME,'body')
    page.send_keys(Keys.END)
    time.sleep(random.randint(5, 8))

# Get the page source and quit the driver
page_source = driver.page_source
driver.quit()

# Use BeautifulSoup to parse the page source
soup = BeautifulSoup(page_source, 'html.parser')

tool_name = []
tool_link = []
type_name = []

# Find and print the titles
names = soup.find_all('a', class_='tool-item-link---new')
for name in names:
    tool_name.append(name.text)

links = soup.find_all('a', class_='tool-item-new-window---new w-inline-block')
for link in links:
    tool_link.append(link.get('href'))


output_data = pd.DataFrame({
    'Tool Name' : tool_name,
    'Link' : tool_link
    
})

print(output_data)
