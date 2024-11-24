import time
from pathlib import Path

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
driver.find_element(By.XPATH,'(//android.view.View[@content-desc="Mark as complete"])[1]').click()

wait = WebDriverWait(driver,10)
wait.until(EC.element_to_be_clickable((By.ID,'com.google.android.apps.tasks:id/sort_order_button')))
driver.find_element(By.ID,'com.google.android.apps.tasks:id/sort_order_button').click()

