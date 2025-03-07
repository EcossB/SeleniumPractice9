import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


@allure.feature("Dropdown")
@allure.story("Selección de Opciones")
def test_dropdown():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://the-internet.herokuapp.com/dropdown")
    try:
        with allure.step("Ubicar y seleccionar opciones en el dropdown"):
            dropdown = Select(driver.find_element(By.ID, "dropdown"))
            dropdown.select_by_visible_text("Option 1")
            selected_option = dropdown.first_selected_option
            assert selected_option.text == "Option 1"

            dropdown.select_by_visible_text("Option 2")
            selected_option = dropdown.first_selected_option
            assert selected_option.text == "Option 2"
    finally:
        driver.quit()
