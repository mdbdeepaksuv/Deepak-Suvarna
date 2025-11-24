'''
css selector    :   To locate the web-elements using any attribute
                    SYNTAX  :   tagname[attr_name="attr_value"]


'''
# import time
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.saucedemo.com/')
# time.sleep(2)
#
# driver.find_element('css selector', 'input[placeholder="Username"]').send_keys('standard_user')
# time.sleep(1)
# driver.find_element('css selector', 'input[type="password"]').send_keys('secret_sauce')
# time.sleep(1)
# driver.find_element('css selector', 'input[type="submit"]').click()

###############################################################################################

#EG2
import time

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://www.facebook.com/r.php?entry_point=login ')
time.sleep(2)

driver.find_element('css selector', 'input[name="firstname"]').send_keys('deepak')
time.sleep(1)
driver.find_element('css selector', 'input[name="lastname"]').send_keys('test')
time.sleep(1)
driver.find_element('css selector', 'input[value="2"]').click()
time.sleep(1)
driver.find_element('css selector', 'input[name="reg_email__"]').send_keys('deepak@mail.com')
time.sleep(1)
driver.find_element('css selector', 'input[name="reg_passwd__"]').send_keys('testpassword')
time.sleep(1)





