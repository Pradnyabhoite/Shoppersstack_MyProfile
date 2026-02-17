from selenium.webdriver.common.by import By

class ProfilePage:

    def __init__(self, driver):
        self.driver = driver

    profile_icon = (By.XPATH, "//div[@class='profile']")
    my_profile_option = (By.XPATH, "//li[text()='My Profile']")
    edit_button = (By.XPATH, "//button[text()='Edit']")
    name_field = (By.ID, "Full Name")
    save_button = (By.XPATH, "//button[text()='Save']")

    def open_profile(self):
        self.driver.find_element(*self.profile_icon).click()
        self.driver.find_element(*self.my_profile_option).click()

    def click_edit(self):
        self.driver.find_element(*self.edit_button).click()

    def update_name(self, name):
        field = self.driver.find_element(*self.name_field)
        field.clear()
        field.send_keys(name)

    def save_profile(self):
        self.driver.find_element(*self.save_button).click()