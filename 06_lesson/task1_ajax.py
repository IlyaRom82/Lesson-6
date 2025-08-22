from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

print("Открываю браузер...")

driver = webdriver.Chrome()

try:
    print("Перехожу на страницу...")
    driver.get("http://uitestingplayground.com/ajax")

    print("Нажимаю на кнопку...")
    button = driver.find_element(By.ID, "ajaxButton")
    button.click()

    print("Ожидаю появления сообщения...")
    wait = WebDriverWait(driver, 15)
    wait.until(
        EC.text_to_be_present_in_element(
            (By.CLASS_NAME, "bg-success"),
            "Data loaded with AJAX get request."
        )
    )

    message_text = driver.find_element(By.CLASS_NAME, "bg-success").text
    print("Сообщение получено:", message_text)

finally:
    driver.quit()
    print("Браузер закрыт.")
