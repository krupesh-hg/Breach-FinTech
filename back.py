import requests
from bs4 import BeautifulSoup

url = "https://rbi.org.in/Scripts/Rules.aspx"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

rules = soup.find_all("li")  # Adjust selector based on actual structure

for rule in rules:
    print(rule.text)
