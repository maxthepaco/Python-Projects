import requests
from bs4 import BeautifulSoup

url = "https://docs.google.com/document/d/e/2PACX-1vTMOmshQe8YvaRXi6gEPKKlsC6UpFJSMAk4mQjLm_u1gmHdVVTaeh7nBNFBRlui0sTZ-snGwZM4DBCT/pub"
response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, 'html5lib')

contents = soup.find_all('tr')

print(contents)