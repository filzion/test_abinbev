from selenium.webdriver import Firefox, Chrome
from selenium.webdriver.chrome.options import Options


def before_all(context):
    context.username = context.config.userdata.get("username")
    context.password = context.config.userdata.get("password")
    context.destination_email = context.config.userdata.get("destination_email")

    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

    context.driver = Chrome(chrome_options=chrome_options)
    context.driver.maximize_window()


def after_all(context):
    context.driver.quit()
