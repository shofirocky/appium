import time
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import By
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.action_chains import ActionChains
from appium import webdriver
desired_caps = {}
desired_caps['deviceName']='Android'
desired_caps['platformName']='Android'
desired_caps['appPackage']='com.google.android.apps.tasks'
desired_caps['appActivity']='.ui.TaskListsActivity'
desired_caps['automationName']='UiAutomator2'
desired_caps['noReset']=ture

driver = webdriver.Remote('http://127.0.0.1:4723',desired_caps)
driver.implicitly_wait(5)
#driver.find_element_by_ID(
