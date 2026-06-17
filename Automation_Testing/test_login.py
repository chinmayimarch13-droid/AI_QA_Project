from selenium import webdriver

def test_homepage():
    driver = webdriver.Chrome()

    driver.get("https://automationexercise.com")

    assert "Automation Exercise" in driver.title

    driver.quit()
