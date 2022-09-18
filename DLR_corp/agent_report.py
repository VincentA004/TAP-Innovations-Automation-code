from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
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
    u1, p1,= (keytouse.decrypt(encpwdbyt))



def main():
    agentReport(u1,p1)
    
def agentReport(username , password):
    if __name__ == "__main__":
        #driver = webdriver.Chrome("chromedriver.exe")

        options = webdriver.ChromeOptions()
        #options.add_argument('--user-data-dir=C:\\Users\\Vince\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 2')
        driver = uc.Chrome(version_main = 102,options = options)
        driver.maximize_window()
        time.sleep(.5)
        driver.get('https://smartcompliance.adp.com/avs/launchapp/#/workspaces/employment-tax//processes')
        u = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"login-form_username")))
        u.send_keys(username,Keys.RETURN)
        p = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"login-form_password")))
        p.send_keys(password,Keys.RETURN)
        proto_url_one = 'https://smartcompliance.adp.com/gateway/v1/tax/taxNotice/taxNotices/{}/AgencyNoticeLetter'
        proto_url_two = 'https://smartcompliance.adp.com/gateway/v1/tax/taxNotice/taxNotices/{}/ResponsePackage'
        file = open('reference_id_agentReport.txt')
        ref_id = file.readlines()
        file_two = open('company_location_agentReport.txt')
        location = file_two.readlines()
        file_three = open('date_agentReport.txt')
        date = file_three.readlines()
        output_file = open('output_agentReport.txt', 'w')
        time.sleep(1)
        for(r,l,d) in zip(ref_id,location,date):
            document_downloader(r,l,d,proto_url_two)
            
           

def document_downloader(r,l,d,proto_url):
    time.sleep(1)
    url = proto_url.format(r.strip())
    py.hotkey('ctrl', 't')
    py.write(url)
    py.press('enter')
    time.sleep(2)
    py.hotkey('ctrl', 's')
    time.sleep(2)
    py.press('right')
    comb = '_An_'+l.strip()+'_'+d.strip()+'_'+r.strip()
    py.write(comb)
    py.press('enter')
    time.sleep(.7)
    py.hotkey('ctrl', 'w')
    time.sleep(3)
    
    
            
            
            
            
            
            
        
        
    
        
        
        
        
    
    

main()