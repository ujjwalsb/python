from selenium import webdriver
from selenium.webdriver.common.Keys import Keys

browser = webdriver.Firefox(executable_path='/home/ujjwal/Downloads/geckodriver')
browser.get('http://nostarch.com')

htmlElem = browser.find_element_by_tag_name('html')

htmlElem.send_keys(keys.End)		# Scrolls Bottom
htmlElem.send_keys(keys.Home)		# Scrolls to top


'''	Some more keys are:
		DOWN, UP, LEFT, RIGHT, ENTER, RETURN,
		PAGE_DOWN, PAGE_UP, ESCAPE, BACK_SPACE
		TAB, F1, F2, ........, F12	'''

browser.back()
browser.forward()
browser.refresh()
browser.quit()