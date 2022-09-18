from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import pyautogui as py
from tkinter import Tk
import os
import pyperclip as pc
import progressbar
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
    run(u1,p1)
    
def run(username , password):
    if __name__ == "__main__":
        file0 = open("index_file.txt", "w")
        file = open('Active_emp_ids-2.txt')
        emp_ids = file.readlines()
        #driver = webdriver.Chrome("chromedriver.exe")
        options = webdriver.ChromeOptions()
        #options.add_argument('--user-data-dir=C:\\Users\\Vince\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1')
        driver = uc.Chrome(version_main = 103 , options = options)
        driver.maximize_window()
        driver.get('https://ireports.adp.com/ng/#/search')
        u = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.ID,"login-form_username")))
        u.send_keys(username,Keys.RETURN)
        p = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"login-form_password")))
        p.send_keys(password,Keys.RETURN)
        try:
            two_factor_login(driver)
        except:
            pass
        time.sleep(1)
        #driver.get('https://ireports.adp.com/ng/#/search')
        
        progress_bar(driver,emp_ids,file0)
        
         #//*[@id="search-table"]/table/tbody/tr[1]/td[3]/ng-component/a
         #//*[@id="search-table"]/table/tbody/tr[1]/td[3]/ng-component/a
        
        
        
        
def document_downloader(driver, id,file0):
    driver.get('https://ireports.adp.com/ng/#/search')
    file0.write(id+"\n")
    try:
        xpath = '//*[@id="search-date-types"]'
        k = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,xpath)))
        k.click()
        xpath = '//*[@id="search-date-types-list"]/div[2]/div[1]'
        j = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,xpath)))
        j.click()
        
        xpath = '//*[@id="search-from-year"]'
        j = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,xpath)))
        j.click()
        time.sleep(1)
        py.write('2015')
        time.sleep(.1)
        py.press('enter')
        
        xpath = '//*[@id="search-from-week"]'
        r = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,xpath)))
        r.click()
        time.sleep(1)
        py.write('1')
        time.sleep(.1)
        py.press('enter')
        
        xpath = '//*[@id="search-to-year"]'
        j = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,xpath)))
        j.click()
        time.sleep(1)
        py.write('2022')
        time.sleep(.1)
        py.press('enter')
        
        xpath = '//*[@id="search-to-week"]'
        j = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,xpath)))
        j.click()
        time.sleep(1)
        py.write('55')
        time.sleep(.1)
        py.press('enter')
        
        xpath = '//*[@id="search-show-available"]'
        i = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,xpath)))
        i.click()
        
        xpath = '//*[@id="search-report-name"]'
        v = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,xpath)))
        v.click()
        time.sleep(1)
        py.write('Checks/Vouchers')
        time.sleep(.1)
        py.press('enter')
        
        xpath = '//*[@id="search-field-filenumber"]/div/input'
        a = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,xpath)))
        file_number = id
        a.send_keys(file_number, Keys.RETURN)
        
        xpath = '//*[@id="search-find"]/div/button'
        o = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,xpath)))
        o.click()
        
        xpath = '//*[@id="search-table"]/table/tbody/tr[1]/td[3]/ng-component/a'
        n = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,xpath)))
        name = n.text
        
        xpath = '//*[@id="search-table"]/table/thead/tr/th[2]/ng-component/div/adp-checkbox'
        t = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,xpath)))
        t.click()
        
        xpath = '//*[@id="search-view-all"]'
        y = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,xpath)))
        y.click()
        
        try:
            two_factor(driver)
        except:
            pass
        
        xpath = '//*[@id="report-viewer-download-btn-search"]'
        z = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,xpath)))
        z.click()
        time.sleep(3)
        file_loader(name, id)
        time.sleep(2)
    except:
        pass
    
    
    
def file_loader(name,c):
    src_path = 'C:\\Users\\Vince\\Downloads'
    dst_path = 'C:\\Users\\Vince\Desktop\\temp_k'
    folder_name = name.strip()+'_'+c.strip()
    path = os.path.join(dst_path, folder_name)
    os.mkdir(path)

    # find out about nameing conventions
    for f in os.listdir(src_path):
        n = path + "\\"+f.strip()
        o = src_path + '\\'+f.strip()
        os.rename(o,n)
    time.sleep(2)
        
        
        
def two_factor(driver):
    time.sleep(1.1)
    username = 'Vincent.allam@tapinnov.com'
    password = 'Helios7004$'
    url2 = 'https://outlook.office.com/mail/'
    xpath = '//*[@id="stepup-channel-list"]/ireports-stepup-communication-channel[3]'
    y = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,xpath)))
    y.click()
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
            xpath = '//*[@id="x_iq22h"]' #verification code location
            c_code = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,xpath))).text
            challenge_codes.append(c_code)
        except:
            pass
    driver.close()
    driver.switch_to.window(original_window)
    xpath = '//*[@id="stepup-verification-code"]/div/input'
    #time.sleep(30)
    y = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,xpath)))
    y.send_keys(challenge_codes[0], Keys.RETURN)
    xpath = '//*[@id="stepup-continue"]'
    y = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,xpath)))
    y.click()
    time.sleep(1)
    
def progress_bar(driver,emp_ids,file0):
    widgets = [' [',
         progressbar.Timer(format= 'elapsed time: %(elapsed)s'),
         '] ',
           progressbar.Bar('*'),' (',
           progressbar.ETA(), ') ',
          ]
  
    bar = progressbar.ProgressBar(max_value=len(emp_ids), 
                              widgets=widgets).start()
    i=0
    
    downloaded_ids = get_downloaded()
    for id in emp_ids:
        time.sleep(1)
        cus_id = id_filler(id.strip())
        if cus_id not in downloaded_ids:
            document_downloader(driver, cus_id , file0)
        else:
            pass
        i = i+1
        bar.update(i)


def id_filler(id):
    prefix = ""
    length = len(id)
    diff = 6-length
    for i in range(diff):
        prefix = prefix + '0'
    new_id = prefix+id
    return new_id
      
def two_factor_login(driver):
    time.sleep(5)
    username = u2
    password = p2
    url2 = 'https://outlook.office.com/mail/'
    xpath = '//*[@id="frmLogin"]/div/div[1]/div[2]/button[2]/div/div[1]'
    h = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,xpath)))
    h.click()
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
            xpath = '//*[@id="x_iq22h"]' #verification code location
            c_code = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,xpath))).text
            challenge_codes.append(c_code)
        except:
            pass
    driver.close()
    driver.switch_to.window(original_window)
    #print(challenge_codes[0])
    xpath = '//*[@id="otpform"]/input'
    f = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,xpath)))
    f.send_keys(challenge_codes[0])
    time.sleep(2)
    py.press('enter')
    time.sleep(1)
    try:
        seq_ques(driver)
    except:
        pass
    time.sleep(5)

def seq_ques(driver):
    xpath = '//*[@id="frmLogin"]/div/div/div[1]'
    sec_ques = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,xpath))).text
    if 'nickname' in sec_ques.lower():
        xpath = '//*[@id="otpform"]/input'
        i = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,xpath)))
        i.send_keys('ADP',Keys.RETURN)
    elif 'mother' in sec_ques.lower():
        xpath = '//*[@id="otpform"]/input'
        i = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,xpath)))
        i.send_keys('US',Keys.RETURN)
    elif 'father' in sec_ques.lower():
        xpath = '//*[@id="otpform"]/input'
        i = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,xpath)))
        i.send_keys('Canada',Keys.RETURN)
    else:
        pass       
 
def get_downloaded():  
    file_downloaded = open('emp_ids_downloaded.txt')
    downloaded_ids = file_downloaded.readlines()
    downloaded_ids_stripped = []
    for x in  downloaded_ids:
        downloaded_ids_stripped.append(x.strip())      
    return downloaded_ids_stripped    
main()