import requests
from bs4 import BeautifulSoup

url = "https://docs.google.com/document/d/e/2PACX-1vTMOmshQe8YvaRXi6gEPKKlsC6UpFJSMAk4mQjLm_u1gmHdVVTaeh7nBNFBRlui0sTZ-snGwZM4DBCT/pub"
response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, 'html5lib')

tableContent = soup.find_all(class_='c0')

del tableContent[0]

print(tableContent[0])