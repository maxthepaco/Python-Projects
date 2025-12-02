import requests
from bs4 import BeautifulSoup

url = "https://docs.google.com/document/d/e/2PACX-1vTMOmshQe8YvaRXi6gEPKKlsC6UpFJSMAk4mQjLm_u1gmHdVVTaeh7nBNFBRlui0sTZ-snGwZM4DBCT/pub"
response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, 'html5lib')

tableContent = soup.select('p')

#print(tableContent)

def stripTags(item):
    return item.get_text(" ", strip=False, types=None)

onlySpans = [stripTags(item) for item in tableContent]

setsOfcords = []

for i in range(5, len(onlySpans), 3):
    row = onlySpans[i:i + 3]
    setsOfcords.append(row)


#Start at [5]

print(setsOfcords)