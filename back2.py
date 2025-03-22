from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time

# Set up Chrome WebDriver
service = Service("C:\\Users\\Krupesh\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")  
driver = webdriver.Chrome(service=service)

# Open RBI Compliance Page
driver.get("https://rbi.org.in/Scripts/Rules.aspx")

# Allow JavaScript to load the page
time.sleep(5)  

# Parse the page with BeautifulSoup
soup = BeautifulSoup(driver.page_source, "html.parser")
driver.quit()

# Extract all compliance-related rules (Adjust selector based on RBI site structure)
rules = [rule.text.strip() for rule in soup.find_all("li")]

print("RBI Compliance Rules:", rules)
