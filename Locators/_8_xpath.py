'''
xpath   :   It is a locator used to locate any element on the application uniquely
            We can locate the elements using attributes, we can locate elements using text, indexing is possible,
            can locate dynamically changing elements
            We can locate any element on the web-application using xpath

There are 2 types of xpath
*   absolute xpath  :   Starts from the root of html
*   relative xpath

'''
import time

# ## Eg1
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-A3-1-3PM-Sep15\files_\css_selector_dup.html')
# time.sleep(2)
#
# driver.find_element('xpath', 'html/body/input[1]').send_keys('Vibha')
# time.sleep(1)
# driver.find_element('xpath', 'html/body/input[2]').send_keys('vibha@12345')

###############################################################################################

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://www.saucedemo.com/')
time.sleep(2)

driver.find_element('xpath', 'html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input').send_keys('standard_user')
time.sleep(1)
driver.find_element('xpath', 'html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input').send_keys('secret_sauce')
time.sleep(1)
driver.find_element('xpath', 'html/body/div/div/div[2]/div[1]/div/div/form/input').click()



















































































