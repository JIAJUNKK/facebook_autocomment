import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

user_name = "Your username"
user_password = "Your password"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.facebook.com/")
driver.maximize_window()

# this is the log in part
email = driver.find_element("name", "email")
for c in user_name:
    email.send_keys(c)
    time.sleep(0.1)
password = driver.find_element("name", "pass")
for c in user_password:
    password.send_keys(c)
    time.sleep(0.1)
login = driver.find_element("name", "login")
login.click()
time.sleep(10)

# opens another after logging in
driver.execute_script("window.open('about:blank', 'secondtab');")
driver.switch_to.window("secondtab")
driver.get("The url of your post")

# commenting starts here 
time.sleep(10)
comment = driver.find_element("xpath", "/html/body/div[1]/div[1]/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[3]/div/div[2]/div/div[1]/div[1]/div[3]/div[2]/div[5]/div/div[2]/div[1]/form/div[1]/div/div[1]")
for i in range(10):
    for char in "bump":
        comment.send_keys(char + Keys.ENTER)
        time.sleep(0.1)
# after 100 seconds it comments again
time.sleep(100) 


