from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

driver = webdriver.Chrome()
driver.get("https://demoqa.com/broken")

images = driver.find_elements(By.TAG_NAME, "img")

print("IMAGENES")
print("---------")

for img in images:
    src = img.get_attribute("src")
    
    if src:
        response = requests.get(src)
        if response.status_code >= 400 or not response.headers[
            "Content-Type"
        ].startswith("image"):
            print(f"imagen invalida: {src}")

links = driver.find_elements(By.TAG_NAME, "a")

print("LINKS")
print("-----")

for link in links:
    href = link.get_attribute("href")

    if href:
        response = requests.get(href)
        if response.status_code >= 400:
            print(f"Link invalido: {href}")

