from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

# Replace with the URL of your form
form_url = "file:///E:/Sanjay/6th%20sem/ST/MP/form.html"  # Assuming your form runs on a local server

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Open the form in the browser
driver.get(form_url)

WebDriverWait(driver, 10).until(EC.url_contains("form.html"))

WebDriverWait(driver, 10).until(EC.title_contains("Google Form clone"))
# Wait for the page to load
#timeout = 10  # seconds
#name_field = WebDriverWait(driver, timeout).until(
 #   EC.presence_of_element_located((By.ID, "name"))
#)
# time.sleep(5)
# Find elements by their IDs 
name_field = driver.find_element(By.ID, "name")
usn_field = driver.find_element(By.ID, "usn")
email_field = driver.find_element(By.ID, "email")
# gender_field = driver.find_element(By.ID, "gender")
male_radio_button = driver.find_element(By.XPATH, "//input[@id='gender' and @value='Male']")
# female_radio_button = driver.find_element(By.XPATH, "//input[@id='gender' and @value='Female']")
phone_field = driver.find_element(By.ID, "phone")
# stream_field = driver.find_element(By.ID, "stream")
stream_select = driver.find_element(By.ID, "stream")
select_stream = Select(stream_select)
college_field = driver.find_element(By.ID, "college")
department_field = driver.find_element(By.ID, "department")
event_select = driver.find_element(By.ID, "event")
select_event = Select(event_select)
username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")
submit_button = driver.find_element(By.ID, "submit")

# Enter sample data (replace with logic to generate test data)
time.sleep(4)
name_field.send_keys("Anonymous")
time.sleep(2)
usn_field.send_keys("4JN21IS200")
time.sleep(2)
email_field.send_keys("user@gmail.com")
time.sleep(2)
male_radio_button.click()
time.sleep(2)
phone_field.send_keys("1234567890")
time.sleep(2)
# stream_field.send_keys("1234567890")
select_stream.select_by_value("BE")
time.sleep(2)
college_field.send_keys("PESIT")
time.sleep(2)
department_field.send_keys("Mechanical")
time.sleep(2)
select_event.select_by_value("1")
time.sleep(2)
username_field.send_keys("ANN_06")
time.sleep(2)
password_field.send_keys("Anonymous@06")
time.sleep(4)
# req_field.send_keys("None")
# time.sleep(2)

# Find the submit button (replace with actual selector if needed)
# submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
# submit_button = driver.find_element(By.ID, "submit")
# submit_button =driver.get("file:///E:/Sanjay/6th%20sem/ST/MP/success.html")
# submit_button = driver.find_element(By.XPATH, "//form[@id='myForm']//button[@type='submit']")


# Click the submit button
submit_button.click()
# try:
#   success_message = WebDriverWait(driver, 5).until(
#       EC.presence_of_element_located((By.CLASS_NAME, "success-message"))
#   )
#   print("Form submitted successfully!")
# except TimeoutException:
#   print("Success message not found. Check form behavior.")

# WebDriverWait(driver, 5).until(EC.title_contains("Success"))
driver.get("file:///E:/Sanjay/6th%20sem/ST/MP/success.html")
WebDriverWait(driver, 5).until(EC.title_contains("Success"))
# Optional: Wait for a confirmation message or page change before closing
# time.sleep(5)  # Wait for 5 seconds (adjust as needed)
print("Done broo")
# Close the browser window
driver.quit()
