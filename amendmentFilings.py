from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import pyautogui as py
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
    global u1, p1
    u1,p1= (keytouse.decrypt(encpwdbyt))



def main():
    run(u1,p1,)
    
def run(username , password):
    if __name__ == "__main__":
        #driver = webdriver.Chrome("chromedriver.exe")
        options = webdriver.ChromeOptions()
        #options.add_argument('--user-data-dir=C:\\Users\\Vince\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1')
        driver = uc.Chrome(version_main = 102 , options = options)
        driver.maximize_window()
        driver.get('https://smartcompliance.adp.com/avs/launchapp/#/workspaces/employment-tax//processes')
        u = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"login-form_username")))
        u.send_keys(username,Keys.RETURN)
        p = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"login-form_password")))
        p.send_keys(password,Keys.RETURN)
        proto_url_af = 'https://smartcompliance.adp.com/avs/launchapp/#/amendment/{}'
        file = open('important.txt')
        ref_id = file.readlines()
        time.sleep(7)
        for(r) in ref_id:
            document_downloader(r,proto_url_af)
        
        
def document_downloader(r,proto_url):
    time.sleep(10)
    url = proto_url.format(r.strip())
    py.hotkey('ctrl', 't')
    py.write(url)
    py.press('enter')
    time.sleep(20)
    #py.moveTo(x = 2285, y=1315)
    #py.click(x = 2285 , y = 1315, clicks = 1 ) # doc 1 type:1
    py.click(x = 2252 , y = 1585, clicks = 1 ) # doc 1 type:2
    time.sleep(5)
    py.hotkey('ctrl', 'w')
    time.sleep(7)


main()