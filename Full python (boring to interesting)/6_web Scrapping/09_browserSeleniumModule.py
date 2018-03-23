
from selenium import webdriver

# Download "geckodriver" from this location (location: lets say Downloads):
	# https://github.com/mozilla/geckodriver/releases
browser = webdriver.Firefox(executable_path='/home/ujjwal/Downloads/geckodriver')
print(type(browser))

browser.get('http://inventwithpython.com')

# It will open the browser in selenium mode.