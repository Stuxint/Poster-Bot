#--------------BLESSED TO MAKE BOT WHICH CREATES CHRISTIAN POSTER!!!!!!!----------------------------------


import undetected_chromedriver as uc
from humancursor import WebCursor
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

web = uc.Chrome()
web.get("https://docs.google.com/document/u/0/")

#--------LOGIN IN PART----------------------

usern = web.find_element('xpath', '//*[@id="identifierId"]')
usern.send_keys('Your Gmail Address')
usern.send_keys(Keys.ENTER)

passw= WebDriverWait(web, 10).until(
                EC.presence_of_element_located(('xpath', '//*[@id="password"]/div[1]/div/div[1]/input'))
            )
passw.send_keys('Your Gmail Password')
passw.send_keys(Keys.ENTER)

#--------CREATING PART----------------------
create= WebDriverWait(web, 20).until(
                EC.presence_of_element_located(('xpath', '//*[@id=":1i"]/div[1]/img'))
            )
create.click()

actions = ActionChains(web)

#1. Center text
actions.key_down(Keys.CONTROL).key_down(Keys.SHIFT).send_keys('e').key_up(Keys.CONTROL).key_up(Keys.SHIFT).perform()

#2. Increase font(x7)
for x in range(7):
    actions.key_down(Keys.CONTROL).key_down(Keys.SHIFT).send_keys('.').key_up(Keys.CONTROL).key_up(Keys.SHIFT).perform()

#3. Write text
actions.send_keys(f'"For God so loved the world that he gave his one\nand only Son, that whoever believes in him shall\nnot perish but have eternal life."').perform()

#4. Add emojis
for x in range(2):
    actions.send_keys(Keys.ENTER).perform()

actions.send_keys("John 3:16").perform()
actions.send_keys(Keys.ENTER).perform()

for x in range(2):
    actions.send_keys("✝️").perform()
    

for x in range(2):
    actions.send_keys("❤️").perform()

#5. Inserting Image
for x in range(2):
    actions.send_keys(Keys.ENTER).perform()

actions.key_down(Keys.ALT).send_keys('/').key_up(Keys.ALT).perform()

time.sleep(2)
actions.send_keys("Insert image using URL").perform()
time.sleep(1)
actions.send_keys(Keys.ENTER).perform()

time.sleep(2)
actions.send_keys("https://as2.ftcdn.net/v2/jpg/05/89/67/07/1000_F_589670799_cscbR8q4pAbFgPKQTgEHF2eKIsrVe9gE.jpg").perform()
actions.send_keys(Keys.ENTER).perform()
time.sleep(1)
for x in range(3):
    actions.send_keys(Keys.TAB).perform()

actions.send_keys(Keys.ENTER).perform()

time.sleep(2)
for x in range(3):
    actions.key_down(Keys.CONTROL).send_keys('-').key_up(Keys.CONTROL).perform()


time.sleep(10)