import pytest
import allure
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.feature("Subida de Archivos")
@allure.story("Subida Exitosa de un Archivo")
def test_file_upload(tmp_path):
    # Crear un archivo de prueba temporal
    test_file = tmp_path / "test_upload.txt"
    test_file.write_text("Este es un archivo de prueba para la subida.")

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://the-internet.herokuapp.com/upload")
    try:
        with allure.step("Seleccionar el archivo para subir"):
            file_input = driver.find_element(By.ID, "file-upload")
            file_input.send_keys(str(test_file))

        with allure.step("Hacer clic en el botón Upload"):
            upload_button = driver.find_element(By.ID, "file-submit")
            upload_button.click()

        with allure.step("Verificar confirmación de subida"):
            wait = WebDriverWait(driver, 10)
            header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h3")))
            assert "File Uploaded!" in header.text
    finally:
        driver.quit()
