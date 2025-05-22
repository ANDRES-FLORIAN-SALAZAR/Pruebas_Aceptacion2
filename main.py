from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument("--disable-gpu")
    # options.add_argument("--headless")
    options.add_argument("--incognito")

    driver = webdriver.Chrome(options=options)
    driver.get("https://demoqa.com/register")
    return driver

def datos_registrarse(driver):
    datos: dict[str, str] = {
        "firstname": "Duvan Andres",
        "lastname": "Florian Salazar",
        "userName": "Andres.0810",
        "password": "123456789",
    }
    
    for campo_id, valor in datos.items():
        driver.find_element(By.ID, campo_id).send_keys(valor)
        time.sleep(1)

def seleccionar_captcha(driver):
    driver.find_element(By.XPATH, "//iframe[contains(@src,https://www.google.com/recaptcha/api2/anchor?ar=1&amp;k=6LdsKacZAAAAAIxY1X8GuHZljebmKWs8JGp97UK7&amp;co=aHR0cHM6Ly9kZW1vcWEuY29tOjQ0Mw..&amp;hl=en&amp;type=image&amp;v=X-oVtzDcTGjZVms4LEgykmCV&amp;theme=light&amp;size=normal&amp;badge=bottomright&amp;cb=r7ycsr3r9v30)]").click()
    time.sleep(0.5)
    
def main():
    driver = get_driver()
    datos_registrarse(driver)
    seleccionar_captcha(driver)
    driver.quit()

if __name__ == "__main__":
    main()