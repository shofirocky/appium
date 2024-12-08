'''
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

driver = webdriver.Remote('http://127.0.0.1:4723',desired_caps)
driver.implicitly_wait(5)
#driver.find_element_by_ID(
driver.find_element(By.ID,"com.google.android.apps.tasks:id/welcome_get_started").click()
driver.find_element(By.ID,"com.google.android.apps.tasks:id/tasks_fab").click()
driver.find_element(By.ID,"com.google.android.apps.tasks:id/add_task_title").send_keys("tasklist")
driver.find_element(By.ID,"com.google.android.apps.tasks:id/add_task_done").click()
driver.find_element(By.XPATH,'(//android.view.View[@content-desc="Mark as complete"])[1]').click()

'''

import time
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver

# Function to set up the Appium driver
def setup_driver():
    """
    Sets up the Appium driver with the desired capabilities.
    :return: The Appium driver instance
    """
    desired_caps = {
        "deviceName": "Android",
        "platformName": "Android",
        "appPackage": "com.google.android.apps.tasks",
        "appActivity": ".ui.TaskListsActivity",
        "automationName": "UiAutomator2"
    }
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    driver.implicitly_wait(5)
    return driver


# Function to start the app
def start_app(driver):
    """
    Clicks the 'Get Started' button to begin.
    """
    driver.find_element(By.ID, "com.google.android.apps.tasks:id/welcome_get_started").click()

# Function to add a task
def add_task(driver, task_name):
    """
    Adds a task to the Google Tasks app.
    :param driver: Appium driver instance
    :param task_name: The name of the task to add
    """
    driver.find_element(By.ID, "com.google.android.apps.tasks:id/tasks_fab").click()
    driver.find_element(By.ID, "com.google.android.apps.tasks:id/add_task_title").send_keys(task_name)
    driver.find_element(By.ID, "com.google.android.apps.tasks:id/add_task_done").click()

# Function to mark a task as complete
def mark_task_complete(driver):
    """
    Marks the first task as complete.
    """
    driver.find_element(By.XPATH, '(//android.view.View[@content-desc="Mark as complete"])[1]').click()

# Main function to execute the test
def main():
    # Setup the driver
    driver = setup_driver()

    try:
        # Perform the workflow
        start_app(driver)
        add_task(driver, "tasklist")
        mark_task_complete(driver)

        print("Test completed successfully!")

    except Exception as e:
        print(f"Test failed: {e}")

    finally:
        # Quit the driver
        driver.quit()

if __name__ == "__main__":
    main()
