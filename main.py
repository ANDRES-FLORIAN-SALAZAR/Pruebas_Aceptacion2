from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument("--incognito")
    return webdriver.Chrome(options=options)

def registrar_usuario(driver):
    driver.get("https://demoqa.com/register")
    time.sleep(2)

    datos = {
        "firstname":"Duvan Andres",
        "lastname": "Florian Salazar",
        "userName": "Andres08",
        "password": "DuvanAndres03#",
    }

    for campo_id, valor in datos.items():
        driver.find_element(By.ID, campo_id).send_keys(valor)
        time.sleep(1)

    # Simulación de captcha
    iframe = driver.find_element(By.XPATH, "//iframe[contains(@src, 'recaptcha')]")
    driver.switch_to.frame(iframe)
    driver.find_element(By.ID, "recaptcha-anchor").click()
    time.sleep(10)
    driver.switch_to.default_content()

    habilitar_boton_register(driver)

    # Registro
    driver.find_element(By.ID, "register").click()
    time.sleep(10)
    driver.save_screenshot("00_registroUsuario.png")

    # Ir a login
    driver.find_element(By.ID, "gotologin").click()
    time.sleep(3)

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
            print("inicio de sesión exitoso.")
        else:
            print("inicio de sesión fallido.")
    except:
        print(" login fallido usuario no encontrado.")
    driver.save_screenshot("02_inicioSesion.png")

def main():
    driver = get_driver()
    registrar_usuario(driver)
    login_usuario(driver)
    validar_login(driver)
    time.sleep(3)
    driver.quit()

if __name__ == "__main__":
    main()