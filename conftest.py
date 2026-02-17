import pytest
from utilities.driver_factory import get_driver
from utilities.config_reader import read_config

@pytest.fixture
def setup():
    config = read_config()
    driver = get_driver()
    driver.get(config["url"])
    yield driver
    driver.quit()