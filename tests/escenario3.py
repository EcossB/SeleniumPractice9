import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.feature("Carga Dinámica")
@allure.story("Visualización del Mensaje Tras Carga")
def test_dynamic_loading():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://the-internet.herokuapp.com/dynamic_loading/1")
    try:
        with allure.step("Hacer clic en el botón Start"):
            start_button = driver.find_element(By.CSS_SELECTOR, "#start button")
            start_button.click()

        with allure.step("Esperar a que se muestre el mensaje 'Hello World!'"):
            wait = WebDriverWait(driver, 10)
            hello_world = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish h4")))
            assert "Hello World!" in hello_world.text
    finally:
        driver.quit()
