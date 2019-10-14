from selenium import webdriver
from selenium.webdriver.common.keys import Keys


url = "http://www.inmet.gov.br/sonabra/pg_dspDadosCodigo_sim.php?QTcxMQ=="

driver = webdriver.Firefox()
driver.get(url)
