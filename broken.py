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
        try:
            response = requests.get(src, timeout=5)
            if response.status_code >= 400 or not response.headers.get("Content-Type", "").startswith("image"):
                print(f"Error: Imagen inválida: {src} (Status: {response.status_code})")
            else:
                print(f"OK: Imagen válida: {src}")
        except requests.RequestException as e:
            print(f"Error al acceder a la imagen {src}: {str(e)}")

links = driver.find_elements(By.TAG_NAME, "a")

print("\nLINKS")
print("-----")

for link in links:
    href = link.get_attribute("href")
    
    if href:
        try:
            response = requests.get(href, timeout=5)
            if response.status_code >= 400:
                print(f"Error: Link inválido: {href} (Status: {response.status_code})")
            else:
                print(f"OK: Link válido: {href}")
        except requests.RequestException as e:
            print(f"Error al acceder al link {href}: {str(e)}")

driver.quit()

