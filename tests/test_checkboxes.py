import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

@allure.feature("Checkboxes")
@allure.story("Verificación y Cambio de Estado")
def test_checkboxes():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://the-internet.herokuapp.com/checkboxes")
    try:
        with allure.step("Obtener lista de checkboxes"):
            checkboxes = driver.find_elements(By.CSS_SELECTOR, "#checkboxes input[type='checkbox']")
            # Alternar el estado de cada checkbox
            for checkbox in checkboxes:
                initial_state = checkbox.is_selected()
                checkbox.click()
                new_state = checkbox.is_selected()
                assert new_state != initial_state
    finally:
        driver.quit()
