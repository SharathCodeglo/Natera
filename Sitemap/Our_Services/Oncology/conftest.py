import pytest
from selenium import webdriver


@pytest.fixture
def setup():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    return driver


# ****Below Methods are applicable only if we want to run the test cases in different browsers
# def setup(browser):
#     if browser == 'chrome':
#         driver = webdriver.Chrome()
#     elif browser == 'firefox':
#         driver = webdriver.Firefox()
#     else:
#         driver = webdriver.Edge()
#     return driver
#
# def pytest_adoption(parser):      # This Will get the value of CLI/Hooks
#     parser.addoption("--browser")\
#
# @pytest.fixture()
# def browser(request):
#     return request.config.getoptiom("--browser")

# ********Pytest HTML Reports**********


# It is hooks for Adding Environment info to HTML Report
# def pytest_configure(config):
#     config._metadata['Project Name'] = 'Natera'
#     config._metadata['Module Name'] = 'Signatera'
#     config._metadata['Tester'] = 'Sharath VR'
#
#
# # It is hooks for Delete/Modify Environment info to HTML Report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)
