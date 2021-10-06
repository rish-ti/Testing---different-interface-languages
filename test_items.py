link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
import time


def test_add_to_basket_button(browser):
	browser.get(link)
	button=browser.find_elements_by_css_selector(".btn-add-to-basket")
	assert button, "There is no button add_to_basket!"