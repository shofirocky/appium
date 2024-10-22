import time
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import By
from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver
desired_caps = {}
desired_caps['deviceName']='Android'
desired_caps['platformName']='Android'
desired_caps['appPackage']='com.google.android.apps.tasks'
desired_caps['appActivity']='.ui.TaskListsActivity'
desired_caps['automationName']='UiAutomator2'

driver = webdriver.Remote('http://127.0.0.1:4723',desired_caps)
driver.implicitly_wait(5)
#driver.find_element_by_ID(
driver.find_element(By.ID,"com.google.android.apps.tasks:id/welcome_get_started").click()
driver.find_element(By.ID,"com.google.android.apps.tasks:id/tasks_fab").click()
driver.find_element(By.ID,"com.google.android.apps.tasks:id/add_task_title").send_keys("tasklist")
driver.find_element(By.ID,"com.google.android.apps.tasks:id/add_task_done").click()
driver.find_element(By.XPATH,'(//android.view.View[@content-desc="Mark as complete"])[2]').click()

#driver.find_element_by_xpath(
#driver.find_element(By_xpath,"(android.view.View[@content-desc="Mark as complete"])[2]").click()
#action = TouchAction(driver)
#action.press(x=500, y=1000).wait(1000).move_to(x=500, y=300).release().perform()
#self.driver.refresh()
#driver.refresh()

