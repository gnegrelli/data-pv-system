from selenium import webdriver
from selenium.webdriver.common.keys import Keys


url = "http://www.inmet.gov.br/sonabra/pg_dspDadosCodigo_sim.php?QTcxMQ=="

driver = webdriver.Firefox()
driver.get(url)

ini_date = driver.find_element_by_name('dtaini')
ini_date.clear()
ini_date.send_keys('30/08/2019')

fin_date = driver.find_element_by_name('dtafim')
fin_date.clear()
fin_date.send_keys('01/10/2019')

re_captcha = driver.find_element_by_name('aleaNum')
re_captcha.clear()
re_captcha.send_keys('2618')
