# import time
#
# ## Eg1
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://demowebshop.tricentis.com/')
# time.sleep(2)
#
# driver.find_element('class name', 'ico-register').click()
# time.sleep(2)
# driver.find_element('class name', 'ico-login').click()
# time.sleep(2)
# driver.find_element('class name', 'ico-cart').click()
#####################################################################################

## Eg2

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-A3-1-3PM-Sep15\files_\css_selector.html')
time.sleep(2)

driver.find_element('class name', 'first_row').send_keys('Shubhangi')
time.sleep(1)
driver.find_element('class name', 'first_row').send_keys('Vibha')
time.sleep(1)
driver.find_element('class name', 'first_row').send_keys('Solai')