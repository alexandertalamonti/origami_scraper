import requests
from bs4 import BeautifulSoup

# get html from site's URL
response = requests.get("https://www.origami-fun.com/origami-instructions.html")
site_text = response.text

# initialize BeautifulSoup Parser
soup = BeautifulSoup(site_text, "html.parser")

# initialize array of origami folds
origami_folds = []

# Find all table rows
rows = soup.find_all('tr')
# Loop through each row
for row in rows:
    # Find the <p> element that contains an <a> tag inside the row
    p = row.find('p')
    
    a = p.find('a')
        
    # If <a> exists, extract and print its text
    if a:
        origami_folds.append(a.text.strip())

print(sorted(origami_folds))