from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_radio_button():

    driver = webdriver.Chrome()
    driver.maximize_window()

    # Open Radio Button page
    driver.get("https://demoqa.com/radio-button")
    time.sleep(2)

    # Click "Impressive"
    driver.find_element(By.XPATH, "//label[text()='Impressive']").click()
    time.sleep(1)

    # Verify result text
    result = driver.find_element(By.CLASS_NAME, "text-success").text
    print("Selected option:", result)

    assert result == "Impressive"

    driver.quit()
