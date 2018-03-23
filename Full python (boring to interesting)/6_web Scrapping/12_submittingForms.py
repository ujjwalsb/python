from selenium import webdriver

browser = webdriver.Firefox(executable_path='/home/ujjwal/Downloads/geckodriver')
browser.get('http://gmail.com')

emailElem = browser.find_element_by_id('identifierId')
emailElem.send_keys('ujjwalsingh15@gmail.com')

passwordElem = browser.find_element_by_id('Passwd')
passwordElem.send_keys('qwerty')

passwordElem.submit()