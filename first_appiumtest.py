import time

from appium import webdriver
desired_caps = {}
desired_caps['deviceName']='Android'
desired_caps['platformName']='Android'
desired_caps['appPackage']='com.vivo.weather'
desired_caps['appActivity']='.WeatherMain'
desired_caps['automationName']='UiAutomator2'

driver = webdriver.Remote('http://127.0.0.1:4723',desired_caps)
driver.implicitly_wait(5)
#driver.find_element_by_ID("com.vivo.weather:id/forecast_hourdata_recyclerview").click()