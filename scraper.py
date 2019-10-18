from selenium import webdriver
from selenium.webdriver.common.keys import Keys


url = "http://www.inmet.gov.br/sonabra/pg_dspDadosCodigo_sim.php?QTcxMQ=="

driver = webdriver.Firefox()
driver.get(url)

# Fill initial date field
ini_date = driver.find_element_by_name('dtaini')
ini_date.clear()
ini_date.send_keys('30/08/2019')

# Fill final date field
fin_date = driver.find_element_by_name('dtafim')
fin_date.clear()
fin_date.send_keys('01/10/2019')

# Save captcha on png
img = driver.find_element_by_tag_name('img')
with open('captcha.png', 'wb') as image:
    image.write(img.screenshot_as_png)

# Fill captcha value field
re_captcha = driver.find_element_by_name('aleaNum')
re_captcha.clear()
re_captcha.send_keys('2618')

# Press enter to go on
re_captcha.send_keys(Keys.RETURN)

# Click on button to display data in csv
btn_dwnload = driver.find_element_by_name('Submit2')
btn_dwnload.click()

# Find body of page
body = driver.find_elements_by_tag_name('body')

# Write content of body on txt file
with open('data.txt', 'w+') as f:
    f.write(body.text)
