from bs4 import BeautifulSoup 
import requests 
import pandas as pd 

url = 'https://en.wikipedia.org/wiki/List_of_national_capitals'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table
table_data = soup.find('table', class_='wikitable')

# Extract headers
table_headers = table_data.find_all('th')
table_headers = [header.text.strip() for header in table_headers]

# Create DataFrame
df = pd.DataFrame(columns=table_headers)

# Extract rows
rows_data =table_data.find_all('tr')
for row in rows_data:
    row_data = row.find_all('td')
    row_data = [data.text.strip() for data in row_data]
   
   # Only add rows that have the correct number of columns
    if len(row_data) == len(table_headers):
        length = len(df)
        df.loc[length] = row_data

# Save to CSV
df.to_csv('countries.csv', index=False)
print('File Saved Successfully!')