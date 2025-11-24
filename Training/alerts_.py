'''
Alerts are not inspectable.
If we are able to inspect it, then it is not an alert.

'''
import time


## Confirmation alert

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://testautomationpractice.blogspot.com/')
time.sleep(2)

driver.find_element('xpath', '//button[text()="Confirmation Alert"]').click()       ## will give alert
time.sleep(2)

alert_obj = driver.switch_to.alert

alert_obj.accept()
time.sleep(2)

driver.find_element('xpath', '//button[text()="Confirmation Alert"]').click()       ## will give alert
time.sleep(2)

alert_obj.dismiss()

############################################################################################################

# ## Simple alert
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//button[text()="Simple Alert"]').click()
# time.sleep(2)
#
# alert_obj = driver.switch_to.alert
#
# alert_obj.accept()
# time.sleep(2)
#
# driver.find_element('xpath', '//button[text()="Simple Alert"]').click()
# time.sleep(2)
# alert_obj.dismiss()

############################################################################################################

# ## prompt alert
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//button[text()="Prompt Alert"]').click()
# time.sleep(2)
#
# alert_obj = driver.switch_to.alert
# alert_obj.send_keys('Aishwarya')
# alert_obj.accept()


############################################################################################################

## Authentication popup

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://the-internet.herokuapp.com/basic_auth')
#
# ## The above url, it will ask for the username and password to launch the application.

##------------------------------------------------------------------------------------------------

## To handle such pop-ups we will give the username and password while launching the application
## SYNTAX   :   https://username:password@url

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://admin:admin@the-internet.herokuapp.com/basic_auth')





































































