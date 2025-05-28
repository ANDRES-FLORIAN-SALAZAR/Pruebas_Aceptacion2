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
        "firstname": "Duvan Andres",
        "lastname": "Florian Salazar",
        "userName": "Andres.0810",
        "password": "Andres.0810",
    }

    for campo_id, valor in datos.items():
        driver.find_element(By.ID, campo_id).send_keys(valor)
        time.sleep(1)

    # generar simulación de captcha
    iframe = driver.find_element(By.XPATH, "//iframe[contains(@src, 'recaptcha')]")
    driver.switch_to.frame(iframe)
    driver.find_element(By.ID, "recaptcha-anchor").click()
    time.sleep(10)
    driver.switch_to.default_content()

    # Habilitar el botón Register de manera manual
    habilitar_boton_register(driver)

    # Hacer clic en el botón Register
    driver.find_element(By.ID, "register").click()
    time.sleep(10)

    # Volver a login
    driver.find_element(By.ID, "gotologin").click()
    time.sleep(2)

def habilitar_boton_register(driver):
    driver.execute_script("document.getElementById('register').disabled = false;")
    time.sleep(1)

def login_usuario(driver):
    driver.find_element(By.ID, "userName").send_keys("Andres.0810")
    driver.find_element(By.ID, "password").send_keys("Andres.0810")
    driver.find_element(By.ID, "login").click()
    time.sleep(3)

def verificar_login(driver):
    try:
        logout_btn = driver.find_element(By.ID, "submit")
        if logout_btn.text.strip().lower() == "log out":
            print("inicio de sesión exitoso.")
        else:
            print("inicio de sesión fallido.")
    except:
        print(" login fallido usuario no encontrado.")

def main():
    driver = get_driver()
    registrar_usuario(driver)
    login_usuario(driver)
    verificar_login(driver)
    driver.quit()

if __name__ == "__main__":
    main()