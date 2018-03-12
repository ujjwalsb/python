from selenium import webdriver

browser = webdriver.Firefox(executable_path='/home/ujjwal/Downloads/geckodriver')
browser.get('http://inventwithpython.com')

linkElem = browser.find_element_by_link_text('Read Online for Free')
linkElem.click()