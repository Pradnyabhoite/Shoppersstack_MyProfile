from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    login_button = (By.ID, "loginBtn")
    email_field = (By.ID, "Email")
    password_field = (By.ID, "Password")
    submit_button = (By.XPATH, "//button[text()='Login']")

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def enter_email(self, email):
        self.driver.find_element(*self.email_field).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def submit_login(self):
        self.driver.find_element(*self.submit_button).click()