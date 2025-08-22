from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/ajax")

    button = driver.find_element(By.ID, "ajaxButton")
    button.click()

    wait = WebDriverWait(driver, 15)

    # Ждём, когда в div.bg-success появится текст
    success_message = wait.until(
        EC.text_to_be_present_in_element(
            (By.CLASS_NAME, "bg-success"),
            "Data loaded with AJAX get request."
        )
    )

    # После успешного ожидания достаём текст
    message_text = driver.find_element(By.CLASS_NAME, "bg-success").text
    print(message_text)

finally:
    driver.quit()
