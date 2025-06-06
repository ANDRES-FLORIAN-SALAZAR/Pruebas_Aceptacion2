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
    print(f"Color inicial: {initial_color}")
    
    WebDriverWait(driver, 10).until(
        lambda d: d.find_element(By.ID, "colorChange").value_of_css_property("color") != initial_color
    )
    new_color = color_button.value_of_css_property("color")
    print(f"Color después del cambio: {new_color}")
    
    if initial_color != new_color:
        print("El color cambió correctamente")
    else:
        print("Error: El color no cambió")

    try:
        
        WebDriverWait(driver, 6).until(
            EC.visibility_of_element_located((By.ID, "visibleAfter"))
        )
        visible_button = driver.find_element(By.ID, "visibleAfter")
        print(f"Botón visibleAfter: {visible_button.text}")
    except:
        print("Error: El botón visibleAfter no apareció")

    try:
        
        WebDriverWait(driver, 6).until(
            EC.element_to_be_clickable((By.ID, "enableAfter"))
        )
        enabled_button = driver.find_element(By.ID, "enableAfter")
        print(f"Botón enableAfter: {enabled_button.text}")
    except:
        print("Error: El botón enableAfter no se habilitó")

    dynamic_elements = driver.find_elements(By.XPATH, "//*[contains(@id, 'dynamic')]")
    for element in dynamic_elements:
        element_id = element.get_attribute("id")
        print(f"ID dinámico encontrado: {element_id}")

    images = driver.find_elements(By.TAG_NAME, "img")
    print("\nIMÁGENES")
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

finally:
    driver.quit()
