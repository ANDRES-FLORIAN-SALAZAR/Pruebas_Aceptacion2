from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

driver = webdriver.Chrome()
driver.get("https://demoqa.com/dynamic-properties")

try:
    
    color_button = driver.find_element(By.ID, "colorChange")
    initial_color = color_button.value_of_css_property("color")

    
    WebDriverWait(driver, 10).until(
        lambda d: d.find_element(By.ID, "colorChange").value_of_css_property("color") != initial_color
    )
    new_color = color_button.value_of_css_property("color")
    print(f"Color inicial: {initial_color}")
    print(f"Color después del cambio: {new_color}")

    images = driver.find_elements(By.TAG_NAME, "img")

    print("IMAGENES")
    print("---------")

    for img in images:
        src = img.get_attribute("src")
        if src:
            try:
                response = requests.get(src, timeout=5)
                if response.status_code >= 400 or not response.headers.get("Content-Type", "").startswith("image"):
                    print(f"Imagen inválida: {src}")
            except requests.RequestException as e:
                print(f"Error al acceder a la imagen {src}: {e}")

    links = driver.find_elements(By.TAG_NAME, "a")

    print("LINKS")
    print("-----")

    for link in links:
        href = link.get_attribute("href")
        if href:
            try:
                response = requests.get(href, timeout=5)
                if response.status_code >= 400:
                    print(f"Link inválido: {href}")
            except requests.RequestException as e:
                print(f"Error al acceder al link {href}: {e}")
finally:
    driver.quit()