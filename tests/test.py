from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# define variables
EMAIL = 'test@gmail.com'
INVALID_EMAIL = 'eqw@test'
EMPTY_EMAIL = ''
PASSWORD = 'test@#WS11'
EMPTY_PASSWORD = ''
FIRST_NAME = 'John'
LAST_NAME = 'Smith'
EMPTY_FIRST_NAME = ''
EMPTY_LAST_NAME = ''

# init driver
driver = webdriver.Chrome(executable_path='chromedriver')

# open the url
driver.get('http://localhost:3000/')

sleep(4)

# check for empty email
email_value = driver.find_element(By.ID, 'email')
email_value.send_keys(EMPTY_EMAIL)
next_button = driver.find_element(By.XPATH, "//button[@type='submit']")
next_button.click()
required_field_msg = driver.find_elements(By.CSS_SELECTOR, "#email+div[class='invalid-feedback']")
assert len(required_field_msg) > 0, 'Expected email field is required'
assert required_field_msg[0].text == 'Required field', 'Expected valid error message'

# check for invalid email
email = driver.find_element(By.ID, 'email')
email.clear()
email.send_keys(INVALID_EMAIL)
next_button = driver.find_element(By.XPATH, "//button[@type='submit']")
next_button.click()
required_field_msg = driver.find_elements(By.CSS_SELECTOR, "#email+div[class='invalid-feedback']")
assert len(required_field_msg) > 0, 'Expected email value is required'
assert required_field_msg[0].text == 'Invalid value', 'Expected valid value'

# check for email
email = driver.find_element(By.ID, 'email')
email.clear()
email.send_keys(EMAIL)

# check for empty password
password_value = driver.find_element(By.ID, 'password')
password_value.send_keys(EMPTY_PASSWORD)
next_button = driver.find_element(By.XPATH, "//button[@type='submit']")
next_button.click()
required_field_msg = driver.find_elements(By.CSS_SELECTOR, "#password+div[class='invalid-feedback']")
assert len(required_field_msg) > 0, 'Expected password field is required'
assert required_field_msg[0].text == 'Required field', 'Expected valid password message'

# check password column
password = driver.find_element(By.ID, 'password')
password.clear()
password.send_keys(PASSWORD)

# check next button
next_button = driver.find_element(By.XPATH, "//button[@type='submit']")
next_button.click()

sleep(3)

# check move to step 2
step2_text = driver.find_element(By.CSS_SELECTOR, 'h1').text
assert step2_text == 'Step 2', 'did not move to step 2'

# check for empty first name
first_name_value = driver.find_element(By.ID, 'firstName')
first_name_value.send_keys(EMPTY_FIRST_NAME)
next_button = driver.find_element(By.XPATH, "//button[@type='submit']")
next_button.click()
required_field_msg = driver.find_elements(By.CSS_SELECTOR, "#firstName+div[class='invalid-feedback']")
assert len(required_field_msg) > 0, 'Expected First Name field is required'
assert required_field_msg[0].text == 'Required field', 'Expected valid first name message'

# check first_name column
first_name = driver.find_element(By.ID, 'firstName')
first_name.clear()
first_name.send_keys(FIRST_NAME)

# check for empty last name
last_name_value = driver.find_element(By.ID, 'lastName')
last_name_value.send_keys(EMPTY_LAST_NAME)
next_button = driver.find_element(By.XPATH, "//button[@type='submit']")
next_button.click()
required_field_msg = driver.find_elements(By.CSS_SELECTOR, "#lastName+div[class='invalid-feedback']")
assert len(required_field_msg) > 0, 'Expected Last Name field is required'
assert required_field_msg[0].text == 'Required field', 'Expected valid last name message'

# check last_name column
last_name = driver.find_element(By.ID, 'lastName')
last_name.clear()
last_name.send_keys(LAST_NAME)

# check next button
next_button = driver.find_element(By.XPATH, "//button[@type='submit']")
next_button.click()

sleep(3)

# check move to step 3
step3_text = driver.find_element(By.CSS_SELECTOR, 'h1').text
assert step3_text == 'Step 3', 'did not move to step 3'

# compare values on step 3
email_value_step3 = driver.find_elements(By.CSS_SELECTOR, 'dd')[0]
first_name_value_step3 = driver.find_elements(By.CSS_SELECTOR, 'dd')[1]
last_name_value_step3 = driver.find_elements(By.CSS_SELECTOR, 'dd')[2]
assert email_value_step3.text == EMAIL, 'Expected value do not match'
assert first_name_value_step3.text == FIRST_NAME, 'Expected value do not match'
assert last_name_value_step3.text == LAST_NAME, 'Expected value do not match'

# check submit button
submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
submit_button.click()

sleep(2)

# check the last page
success_text = driver.find_element(By.CSS_SELECTOR, 'h1').text
assert success_text == 'Success!', 'Job is not done'

driver.quit()
