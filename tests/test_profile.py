from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from utilities.config_reader import read_config

def test_update_profile(setup):
    driver = setup
    config = read_config()

    login = LoginPage(driver)
    profile = ProfilePage(driver)

    login.enter_email(config["username"])
    login.enter_password(config["password"])
    login.submit_login()

    profile.open_profile()
    profile.click_edit()
    profile.update_name("Pradnya Test")
    profile.save_profile()

    assert "Profile" in driver.title