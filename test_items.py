import time
link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/."

def test_find_items(browser):
    browser.get(link)
    browser.implicitly_wait(10)
    buttn = browser.find_element_by_css_selector(".btn-add-to-basket")
    assert buttn is not None, 'Кнопка не найдена!'