from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.keys import Keys
import time
import random
import re
from bs4 import BeautifulSoup
import requests
import pandas as pd

# Set up the Chrome WebDriver service
service = Service('chromedriver.exe')

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# URL to scrape
url = 'https://www.purelocal.com.au/sydney'

# Open the URL in the browser
driver.get(url)

# Add a sleep time to ensure all elements are loaded
time.sleep(5)

# Scroll down the page multiple times to load more content
for i in range(3):
    page = driver.find_element(By.TAG_NAME, "body")
    page.send_keys(Keys.END)
    time.sleep(random.randint(3,5))

# Find all links to business detail pages
links = driver.find_elements(By.XPATH, "//div[@class='hp6']/a")
links = [link.get_attribute('href') for link in links]

# Compile regular expressions to extract business name and official website
bussiness_name_regex = re.compile(r'Business Name\s*(.*?)Official Website', re.S)
offical_website_regex = re.compile(r'Official Website\s*(.*?)Contact Us', re.S)


# Initialize an empty list to store the extracted data
all_data = []

# Iterate through the links and extract data
for link in links:
    response = requests.get(link)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        text_content = soup.select_one('#business-contact-details').text

        bussiness_name_match = bussiness_name_regex.search(text_content)
        offical_website_match = offical_website_regex.search(text_content)
        

        extratced_data = {
            'Bussiness Name': bussiness_name_match.group(1).strip() if bussiness_name_match else None,
            'Offical Website': offical_website_match.group(1).strip() if offical_website_match else None,
            
        }
        all_data.append(extratced_data)

# Create a DataFrame from the extracted data and save it to a CSV file
df = pd.DataFrame(all_data)
df.to_csv('extracted_data.csv', index=False, encoding='utf-8')

# Close the browser
driver.quit()

