
from selenium import webdriver

browser = webdriver.Firefox(executable_path='/home/ujjwal/Downloads/geckodriver')
browser.get('http://inventwithpython.com')

try:
	elem1 = browser.find_element_by_class_name('jumbotron')
	print('Found <%s> element with class name! ' %(elem1.tag_name))

	elem2 = browser.find_element_by_css_selector('jumbotron')
	print('Found <%s> element with class name! ' %(elem2.tag_name))

	elem3 = browser.find_element_by_id('jumbotron')
	print('Found <%s> element with class name! ' %(elem3.tag_name))

	elem4 = browser.find_element_by_link_text('jumbotron')
	print('Found <%s> element with class name! ' %(elem4.tag_name))

	elem5 = browser.find_element_by_partial_link_test('jumbotron')
	print('Found <%s> element with class name! ' %(elem5.tag_name))

	elem6 = browser.find_element_by_name('jumbotron')
	print('Found <%s> element with class name! ' %(elem6.tag_name))

	elem7 = browser.find_element_by_tag_name('jumbotron')
	print('Found <%s> element with class name! ' %(elem7.tag_name))

except:
	print('Was not able to find elemt with that name.')