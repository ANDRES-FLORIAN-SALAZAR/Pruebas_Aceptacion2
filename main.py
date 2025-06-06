from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument("--incognito")
    return webdriver.Chrome(options=options)

def registrar_usuario(driver):
    driver.get("https://demoqa.com/register")
    time.sleep(2)

    datos = {
        "firstname": "Duvan Andres",
        "lastname": "Florian Salazar",
        "userName": "Andres08",
        "password": "DuvanAndres03#",
    }

    for campo_id, valor in datos.items():
        driver.find_element(By.ID, campo_id).send_keys(valor)
        time.sleep(1)

    try:
        iframe = driver.find_element(By.XPATH, "//iframe[contains(@src, 'recaptcha')]")
        driver.switch_to.frame(iframe)
        driver.find_element(By.ID, "recaptcha-anchor").click()
        time.sleep(10)
        driver.switch_to.default_content()
    except:
        print("⚠️ No se pudo interactuar con el CAPTCHA.")

    habilitar_boton_register(driver)
    driver.find_element(By.ID, "register").click()
    time.sleep(10)
    driver.save_screenshot("00_registroUsuario.png")

    try:
        driver.find_element(By.ID, "gotologin").click()
        time.sleep(3)
    except:
        print("⚠️ No se pudo ir al login desde la pantalla de registro.")

def habilitar_boton_register(driver):
    driver.execute_script("document.getElementById('register').disabled = false;")
    time.sleep(1)

def login_usuario(driver):
    driver.find_element(By.ID, "userName").send_keys("Andres08")
    driver.find_element(By.ID, "password").send_keys("DuvanAndres03#")
    driver.find_element(By.ID, "login").click()
    time.sleep(3)
    driver.save_screenshot("01_loginUsuario.png")

def validar_login(driver):
    try:
        logout_btn = driver.find_element(By.ID, "submit")
        if logout_btn.text.strip().lower() == "log out":
            print("✅ Inicio de sesión exitoso.")
        else:
            print("❌ Inicio de sesión fallido.")
    except:
        print("❌ Login fallido, usuario no encontrado.")
    driver.save_screenshot("02_inicioSesion.png")

def verificar_broken_links_y_imagenes(driver):
    driver.get("https://demoqa.com/broken")
    time.sleep(3)

    print("🔍 Verificando imágenes...")
    imagenes = driver.find_elements(By.TAG_NAME, "img")
    for img in imagenes:
        src = img.get_attribute("src")
        if src:
            try:
                r = requests.get(src)
                status = r.status_code
                print(f"Imagen: {src} ➜ Estado: {status}")
            except Exception as e:
                print(f"❌ Imagen rota: {src} ➜ Error: {e}")

    print("\n🔍 Verificando enlaces...")
    enlaces = driver.find_elements(By.TAG_NAME, "a")
    for enlace in enlaces:
        href = enlace.get_attribute("href")
        if href:
            try:
                r = requests.get(href)
                status = r.status_code
                print(f"Enlace: {href} ➜ Estado: {status}")
            except Exception as e:
                print(f"❌ Enlace roto: {href} ➜ Error: {e}")
    driver.save_screenshot("03_broken_links_images.png")

def probar_propiedades_dinamicas(driver):
    driver.get("https://demoqa.com/dynamic-properties")
    time.sleep(3)

    print("\n🧪 Verificando propiedades dinámicas...")

    try:
        color_button = driver.find_element(By.ID, "colorChange")
        initial_color = color_button.value_of_css_property("color")
        print(f"Color inicial del botón: {initial_color}")
    except:
        print("❌ Botón con cambio de color no encontrado.")

    try:
        time.sleep(6)  # Esperar lo suficiente para que aparezcan los elementos dinámicos
        visible_button = driver.find_element(By.ID, "visibleAfter")
        if visible_button.is_displayed():
            print("✅ Botón visible después del retraso detectado.")
    except:
        print("❌ Botón visible después del retraso NO detectado.")

    try:
        enabled_button = driver.find_element(By.ID, "enableAfter")
        estado = "habilitado" if enabled_button.is_enabled() else "deshabilitado"
        print(f"Estado del botón habilitado después del retraso: {estado}")
    except:
        print("❌ Botón habilitado después del retraso no detectado.")

    # Verificar si hay IDs autogenerados (aleatorios)
    todos = driver.find_elements(By.XPATH, "//*")
    autogen_ids = [el.get_attribute("id") for el in todos if el.get_attribute("id") and len(el.get_attribute("id")) >= 10 and any(char.isdigit() for char in el.get_attribute("id"))]
    print(f"🔎 IDs posiblemente autogenerados encontrados: {autogen_ids}")
    driver.save_screenshot("04_dynamic_properties.png")

def main():
    driver = get_driver()
    try:
        registrar_usuario(driver)
        login_usuario(driver)
        validar_login(driver)
        verificar_broken_links_y_imagenes(driver)
        probar_propiedades_dinamicas(driver)
    finally:
        time.sleep(3)
        driver.quit()

if __name__ == "__main__":
    main()