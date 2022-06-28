from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# init driver
service = Service(executable_path="/Users/labzizihind/PycharmProjects/PythonTesting/features/chromedriver 2")
driver = webdriver.Chrome(service=service)

# open the url
driver.get("https://www.demoblaze.com/")
driver.maximize_window()
driver.implicitly_wait(5)


# # Sign up

driver.find_element(By.ID, "signin2").click()
driver.find_element(By.ID, "sign-username").send_keys('yassinenehri')
driver.find_element(By.ID, "sign-password").send_keys('yassine1985')
driver.find_element(By.CSS_SELECTOR, "button[onclick='register()']").click()


# # Alert Accept

WebDriverWait(driver, 5).until(EC.alert_is_present())
driver.switch_to.alert.accept()





# Log In

driver.find_element(By.ID, "login2").click()
driver.find_element(By.ID, "loginusername").send_keys('yassinenehri')
driver.find_element(By.ID, "loginpassword").send_keys('yassine1985')
driver.find_element(By.CSS_SELECTOR, "button[onclick='logIn()']").click()
driver.refresh()


# Adding product one into cart

driver.find_element(By.XPATH, "//*[contains(text(),'Samsung galaxy s6')]").click()

#Add to cart

driver.find_element(By.CSS_SELECTOR, "a[onclick='addToCart(1)']").click()

# Accept Alert

WebDriverWait(driver, 5).until(EC.alert_is_present())
driver.switch_to.alert.accept()
driver.back()
driver.back()
driver.refresh()

# Adding product 2 into cart

driver.find_element(By.XPATH, "//*[contains(text(), 'Nexus 6')]").click()
#Add to cart
driver.find_element(By.CSS_SELECTOR, "a[onclick='addToCart(3)']").click()

# Click on Cart item
driver.find_element(By.ID, "cartur").click()

# Verify cart has 2 items
# count = len(driver.find_elements(By.CSS_SELECTOR, "tr.success"))
# assert count == 2, f'Error! cart suppose to have{count}'

# Place order
driver.find_element(By.CSS_SELECTOR, "button.btn.btn-success").click()

# Fill the form
driver.find_element(By.ID, "name").send_keys('yassine')
driver.find_element(By.ID, "country").send_keys('united states')
driver.find_element(By.ID, "city").send_keys('orlando')
driver.find_element(By.ID, "card").send_keys('123456')
driver.find_element(By.ID, "month").send_keys('july')
driver.find_element(By.ID, "year").send_keys('2022')

# Cancel
driver.find_element(By.CSS_SELECTOR, "button.btn.btn-secondary").click()

# Delete items from cart
driver.find_element(By.XPATH, "//a[text()='Delete']").click()
driver.find_element(By.XPATH, "//a[text()='Delete']").click()

# Log in Again

driver.find_element(By.ID, "login2").click()
driver.find_element(By.ID, "loginusername").send_keys('yassinenehri')
driver.find_element(By.ID, "loginpassword").send_keys('yassine1985')
driver.find_element(By.CSS_SELECTOR, "button[onclick='logIn()']").click()

# Click cart
driver.find_element(By.ID, "cartur").click()

# Verify cart is empty
count = len(driver.find_elements(By.ID, "tbodyid"))
assert count == 0, f'Error! cart suppose to have{count}'

#Back
driver.back()

#Add to cart
driver.find_element(By.CSS_SELECTOR, "button.btn.btn-success").click()

# Delete item
driver.find_element(By.XPATH, "//a[text()='Delete']").click()

# Verify cart is empty
count = len(driver.find_elements(By.ID, "tbodyid"))
assert count == 0, f'Error! cart suppose to have{count}'

# Logout
driver.find_element(By.ID, "logout2").click()

driver.quit()

















