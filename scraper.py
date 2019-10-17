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

# Fill captcha value field
re_captcha = driver.find_element_by_name('aleaNum')
re_captcha.clear()
re_captcha.send_keys('2618')

# Press enter to go on
re_captcha.send_keys(Keys.RETURN)
