import time
import re
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os


# Function to check if a free spot is available
def is_spot_available():
    driver.get('https://students.technion.ac.il/local/technionsearch/search')
    # Find the element to enter input
    input_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'id_course_name')))
    # Enter your desired input
    input_element.send_keys('236350')
    # Find the element to click
    click_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'id_submitbutton')))
    # Click the element
    click_element.click()
    time.sleep(2)
    # Find element by ID
    element = driver.find_element(By.ID, 'courses_results-table_r0_c3')
    # Get the text content of the element
    text = element.text
    # Define the pattern to match "x spots available"
    pattern = r'(\d+) מקומות פנויים'
    # Search for the pattern in the text
    match = re.search(pattern, text)
    if match:
        return True
    else:
        return False

def register():
    # Main script loop
    while True:
        # # Refresh the page after a random delay
        refresh_delay = random.randint(30, 60)  # Choose a random delay between 5 and 10 seconds
        time.sleep(refresh_delay)
        driver.refresh()
        # Check if a free spot is available
        if is_spot_available():
            # Navigate to the registration page
            driver.get('https://students.technion.ac.il/local/tregister/cart')

            # Submit the registration form
            try:
                # Modify the following lines to interact with the registration form elements
                submit_button = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, 'process_cart_item_request'))
                )
                submit_button.click()
                break  # Exit the loop if successfully registered
            except:
                pass
        else:
            pass

if __name__ == '__main__':

    #prepare page
    homedir = os.path.expanduser("~")
    webdriver_service = Service(f"{homedir}/usr/local/bin/chromedriver")
    # save login session so i dont have to log in again every run
    chrome_options = Options()
    user_data_directory = ""
    chrome_options.add_argument(f"user-data-dir={user_data_directory}\\userdata")
    # Create a ChromeDriver instance using the Service object
    driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)
    # Open the first page to check for a free spot
    driver.get('https://students.technion.ac.il/local/technionsearch/search')

    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'page-local-technionsearch-search')))
    element.click()
    driver.get('https://students.technion.ac.il/auth/oidc/')
    # element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'tileMenu0')))
    # element.click()
    #

    time.sleep(3)

    # driver.get('https://students.technion.ac.il/local/technionsearch/search')
    # # Find the element to enter input
    # input_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'id_course_name')))
    # # Enter your desired input
    # input_element.send_keys('236350')
    # # Find the element to click
    # click_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'id_submitbutton')))
    # # Click the element
    # click_element.click()

    # time.sleep(3)

    register()

