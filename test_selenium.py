import logging
from selenium import webdriver
from selenium.webdriver.common.by import By

# Configuración básica del logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='test_execution.log',
                    filemode='w')

logging.info("Inicio de la prueba con Selenium.")

# Inicializar el WebDriver
driver = webdriver.Chrome()
logging.info("Navegador Chrome iniciado.")

try:
    driver.get("https://www.ejemplo.com")
    logging.info("Navegador a la URL: https://www.ejemplo.com")

    # Interactuar con un elemento
    elemento = driver.find_element(By.ID, "boton-login")
    elemento.click()
    logging.info("Se hizo clic en el botón de login.")

except Exception as e:
    logging.error(f"Se produjo un error: {e}")

finally:
    driver.quit()
    logging.info("Navegador cerrado. Fin de la prueba.")
