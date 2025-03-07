import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.feature("Autenticación")
@allure.story("Inicio de Sesión Exitoso")
def test_login_success():
    driver = webdriver.Chrome()  # Asegúrate de tener ChromeDriver configurado
    driver.maximize_window()
    driver.get("http://the-internet.herokuapp.com/login")
    try:
        with allure.step("Ingresar usuario y contraseña válidos"):
            username_input = driver.find_element(By.ID, "username")
            password_input = driver.find_element(By.ID, "password")
            username_input.send_keys("tomsmith")
            password_input.send_keys("SuperSecretPassword!")

        with allure.step("Hacer clic en el botón Login"):
            login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")
            login_button.click()

        with allure.step("Esperar la redirección y verificar mensaje de éxito"):
            wait = WebDriverWait(driver, 10)
            flash_element = wait.until(EC.visibility_of_element_located((By.ID, "flash")))
            assert "You logged into a secure area!" in flash_element.text
    finally:
        driver.quit()
