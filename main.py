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
        
    # If <a> exists, extract and print its text and attach the link
    if a:
        fold_name = append(a.text.strip())
        fold_link = a['href']
        origami_folds.append((fold_name,fold_link))

# sort array alphabetically by first element
origami_folds.sort(key=lambda x: x[0])

# loop through the array to print result
for fold in origami_folds:
    print(f"{fold[0]}, {fold[1]}")
