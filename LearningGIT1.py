# for i in range(1,10):
#  if i%2==0:
#     print('even')
# else:
#     print('odd')


#
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




