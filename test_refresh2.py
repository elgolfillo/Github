from selenium import webdriver
import time
import urllib
import urllib2


def refresca2():
    driver = webdriver.firefox()
    driver.get("http://www.as.com")
    driver.refresh()
    return
    
    
refresca2()