from bs4 import BeautifulSoup 
import requests 
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find('table', class_='wikitable')

# Extract table headers
table_header = table.find_all('th')
table_titles = [title.text.strip() for title in table_header]

# Create DataFrame with the extracted headers
df = pd.DataFrame(columns=table_titles)

# Extract table rows
column_data = table.find_all('tr')

for row in column_data:
    row_data = row.find_all('td')
    individual_raw_data = [data.text.strip() for data in row_data]
    
    # Only add rows that have the correct number of columns
    if len(individual_raw_data) == len(table_titles):
        length = len(df)
        df.loc[length] = individual_raw_data

print(df)
df.to_csv('test_world.csv', index=False)

    



