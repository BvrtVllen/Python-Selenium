'''
Basic test
'''

# import pytest
from selenium.webdriver.common.by import By



URL = 'https://testqastudio.me/'
def test_smoke(browser):
    '''
    SMK-1. Smoke test
    '''
    browser.get(url=URL)

    element = browser.find_element(by=By.CSS_SELECTOR, value = '[class*="post-11341"]')
    element.click()

    sku = browser.find_element(by=By.CSS_SELECTOR, value = '[class="sku"]')
    
    assert sku.text == 'C0MSSDSUM7' , 'Unexpected SKU for "ДИВВИНА Журнальный столик"'