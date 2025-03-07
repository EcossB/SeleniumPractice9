import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.feature("Autenticación")
@allure.story("Inicio de Sesión Fallido")
def test_login_failure():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://the-internet.herokuapp.com/login")
    try:
        with allure.step("Ingresar credenciales inválidas"):
            username_input = driver.find_element(By.ID, "username")
            password_input = driver.find_element(By.ID, "password")
            username_input.send_keys("usuarioInvalido")
            password_input.send_keys("claveErronea")

        with allure.step("Hacer clic en el botón Login"):
            login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")
            login_button.click()

        with allure.step("Esperar y verificar mensaje de error"):
            wait = WebDriverWait(driver, 10)
            flash_element = wait.until(EC.visibility_of_element_located((By.ID, "flash")))
            assert "Your username is invalid!" in flash_element.text
    finally:
        driver.quit()
