from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import pyautogui as py
import datetime as dt
from cryptography.fernet import Fernet
  
def password_decryptor():
    with open('encryptedPWD.txt') as f:
        encpwd = ''.join(f.readlines())
        encpwdbyt = bytes(encpwd, 'utf-8')
    f.close()

    with open('refKey.txt') as f:
        refKey = ''.join(f.readlines())
        refKeybyt = bytes(refKey, 'utf-8')
    f.close()
    keytouse = Fernet(refKeybyt)
    global u1, p1, u2, p2 
    u1, p1, u2, p2 = (keytouse.decrypt(encpwdbyt))
    
def main():
    run()

def run():
    url = "https://secure.paycor.com/onlinereports/index.html#/CurrentReports"
    website_username = u1
    website_password = p1
    if __name__ == "__main__":
        options = webdriver.ChromeOptions()
        driver = uc.Chrome(version_main = 103,options = options)
        driver.maximize_window()
        time.sleep(.5)
        driver.get(url)
        u = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="Username"]')))
        u.send_keys(website_username)
        p = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="Password"]')))
        p.send_keys(website_password,Keys.RETURN)
        two_factor(driver)
        driver.get(url)
        time.sleep(5)
        client_ids = []
        for x in range(1,50):
            xpath = f'//*[@id="root"]/div/div/div/div[2]/div/div[2]/div[2]/div/div/table/tbody/tr[{x}]/td[1]' # client_id location
            try:
                id = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,xpath))).text
            except:
                break
            client_ids.append(id)
        time.sleep(.2)
        for i in client_ids:
            try:
                driver.get(url)
                xpath = '//*[@id="root"]/div/div/div/div[2]/div/div[2]/div[2]/div/div/div/form/div/div[2]/input' #id textbox 
                k = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,xpath)))
                k.send_keys(i)
                b = driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div/div[2]/div/div[2]/div[2]/div/div/div/form/div/span') # open button 
                b.click()
                xpath ='//*[@id="root"]/div/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[3]/div[2]/a' #by report name
                a = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,xpath)))
                a.click()
                row,col = get_jobCost_index(driver)
                xpath = f'//*[@id="root"]/div/div/div/div[2]/div/div[2]/div[2]/div/div/form/div/div[3]/div[{row}]/div[{col}]/div/input' # Job Costing Export checkbox
                x = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,xpath)))
                x.click()
                xpath = '//*[@id="root"]/div/div/div/div[2]/div/div[2]/div[2]/div/div/form/div/div[1]/div/div/div[1]/input' # start date box
                r = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,xpath)))
                target_date = date_math()
                r.send_keys(Keys.CONTROL + "a")
                r.send_keys(Keys.DELETE)
                time.sleep(.2)
                r.send_keys(target_date)
                xpath = '//*[@id="root"]/div/div/div/div[2]/div/div[2]/div[2]/div/div/form/div/div[4]/div[1]/span/a' # open button
                b = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,xpath)))
                b.click()
                xpath = '//*[@id="selectAll"]' # selectAll check box
                c = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,xpath)))
                c.click()
                xpath = '//*[@id="root"]/div/div/div/div[2]/div/div[2]/div[2]/div/div/form/div/div[2]/span[2]/a' # download button
                d = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,xpath)))
                d.click()
                time.sleep(1)
            except:
                pass
        #print(len(client_ids))

        

def date_math():
    today = dt.date.today()
    week_ago = today - dt.timedelta(days=7)
    start_date = week_ago.strftime("%m/%d/%Y")
    return start_date

def get_jobCost_index(driver):
    for x in range(1,500):
        xpath = f'//*[@id="root"]/div/div/div/div[2]/div/div[2]/div[2]/div/div/form/div/div[3]/div[{x}]/div[1]/div/label' # col 1
        xpath2 = f'//*[@id="root"]/div/div/div/div[2]/div/div[2]/div[2]/div/div/form/div/div[3]/div[{x}]/div[2]/div/label' # col 2
        try:
            name = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,xpath))).text
            name2 = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,xpath2))).text
        except:
            break
        if(name == 'Job Costing Export'):
            return x,1
        elif(name2 == 'Job Costing Export'):
            return x,2

def two_factor(driver):
    time.sleep(5)
    username = u2
    password = p2
    url2 = 'https://outlook.office.com/mail/'
    original_window = driver.current_window_handle
    driver.switch_to.new_window('tab')
    driver.get(url2)
    xpath = '//*[@id="i0116"]' #username box
    l = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,xpath)))
    l.send_keys(username,Keys.RETURN)
    xpath = '//*[@id="i0118"]' #password box
    p = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,xpath)))
    p.send_keys(password,Keys.RETURN)
    py.press('tab')
    time.sleep(.85)
    py.press('enter')
    time.sleep(1)
    py.press('enter')
    time.sleep(7)
    mail_list = driver.find_elements(By.XPATH, '//*[contains(@class,"ZtMcN")]') # all mails
    challenge_codes = []
    for i in range(5):
        try:
            mail_list[i].click()
            xpath = '//*[@id="ReadingPaneContainerId"]/div/div/div/div[2]/div/div/div[1]/div/div/div/div/div[3]/div/div/div/div[2]/table/tbody/tr/td/center/table[2]/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/span/span' #verification code location
            c_code = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,xpath))).text
            challenge_codes.append(c_code)
        except:
            pass
    driver.close()
    driver.switch_to.window(original_window)
    #print(challenge_codes[0])
    xpath = '//*[@id="ChallengeCode"]'
    f = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,xpath)))
    f.send_keys(challenge_codes[0])
    time.sleep(2)
    py.press('enter')
    time.sleep(5)
main()