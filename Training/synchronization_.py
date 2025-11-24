import time

# ## using time.sleep()
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-A3-1-3PM-Sep15\files_\loading.html')
# time.sleep(20)
#
# driver.find_element('xpath', '//input[@name="fname"]').send_keys('Jaya')
# time.sleep(1)
# driver.find_element('xpath', '//input[@name="lname"]').send_keys('shree')

#############################################################################################################

# ## implicit_wait
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-A3-1-3PM-Sep15\files_\loading.html')
# driver.implicitly_wait(30)
# driver.find_element('xpath', '//input[@name="fname"]').send_keys('Jaya')
# time.sleep(1)
# driver.find_element('xpath', '//input[@name="lname"]').send_keys('shree')

# #############################################################################################################
#
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-A3-1-3PM-Sep15\files_\progressbar.html')
# time.sleep(2)
#
# driver.find_element('xpath', '//button[text()="Click Me"]').click()
# time.sleep(40)
# driver.find_element('xpath', '//button[text()="Click Me"]').click()
#


#############################################################################################################


from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)
driver.implicitly_wait(45)

driver.get(r'C:\Users\DELL\PycharmProjects\Selenium_Training\Fiiles\progressbar.html')
time.sleep(2)

driver.find_element('xpath', '//button[text()="Click Me"]').click()

driver.find_element('xpath', '//div[text()="100%"]')
time.sleep(2)
driver.find_element('xpath', '//button[text()="Click Me"]').click()






















































