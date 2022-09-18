from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import pyautogui as py
import os
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
        #driver = webdriver.Chrome("chromedriver.exe")
        emp_names = csv_reader()
        options = webdriver.ChromeOptions()
        #options.add_argument('--user-data-dir=C:\\Users\\Vince\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 2')
        driver = uc.Chrome(version_main = 103,options = options)
        driver.maximize_window()
        time.sleep(.5)
        driver.get('https://workforcenow.adp.com/theme/unified.html#/Process/pracPerformance')
        #xpath = '//*[@id="login-form_username"]'
        time.sleep(3)
        py.write(username)
        py.press('enter')
        p = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"login-form_password")))
        p.send_keys(password,Keys.RETURN)
        try:
            two_factor(driver)
        except:
            pass
        driver.get('https://workforcenow.adp.com/theme/unified.html#/Process/pracPerformance')
        time.sleep(30) #Change to old ui in this time

        xpath =  '//*[@id="PerformanceDashAnnual.clickHereLink"]'
        z = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,xpath)))
        z.click()

        xpath =  '//*[@id="PerfDashboardHistoricalReviews.historicalFromDate"]'
        d = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,xpath)))
        start_date = '01/01/2018'
        d.send_keys(start_date)
        d.send_keys(Keys.CONTROL + "a")
        d.send_keys(Keys.DELETE)
        time.sleep(.2)
        d.send_keys(start_date)

        xpath =  '//*[@id="PerfDashboardHistoricalReviews.historicalToDate"]'
        e = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,xpath)))
        end_date = '2/20/2023'
        e.send_keys(end_date)
        e.send_keys(Keys.CONTROL + "a")
        e.send_keys(Keys.DELETE)
        time.sleep(.2)
        e.send_keys(end_date)

        xpath =  '//*[@id="PerfDashboardHistoricalReviews.historicalReviewType"]'
        f = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,xpath)))
        review_type = 'Disciplinary Review'
        f.send_keys(Keys.CONTROL + "a")
        f.send_keys(Keys.DELETE)
        time.sleep(.2)
        f.send_keys(review_type)

        xpath = '//*[@id="PerfDashboardHistoricalReviews.historical"]'
        c = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,xpath)))
        c.click()


        progress_bar(emp_names,driver)



def get_docs(emp_name,driver):
    xpath =  '//*[@id="PerfDashboardHistoricalReviews.historicalEmployeeName"]'
    n = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,xpath)))
    n.send_keys(Keys.CONTROL + "a")
    n.send_keys(Keys.DELETE)
    time.sleep(.2)
    n.send_keys(emp_name)

    xpath = '//*[@id="PerfDashboardHistoricalReviews.searchButton.node"]'
    s = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,xpath)))
    s.click()
    
    for i in range(1,15):
            try:
                download_docs(i,driver)
            except:
                break
    file_loader(emp_name)



def download_docs(number,driver):
    #//*[@id="PerfDashboardHistoricalReviews.historicalReviewsGrid_1_10"]/div/div/span
    xpath = f'//*[@id="PerfDashboardHistoricalReviews.historicalReviewsGrid_{number}_10"]'
    s = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,xpath)))
    s.click()
    xpath = "//*[@id='wfn_body']/div/div[contains(text(),'View Notice')]"
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,xpath)))
    element.click()
    time.sleep(1)

    xpath = '//*[@id="PerfDiscNotice.perfPreview.node"]'
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,xpath)))
    element.click()

    xpath = '//*[@id="PerformanceMenu.PerformanceMenus.node"]/table/tr[1]/td[2]/span[1]/div/span[2]'
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,xpath)))
    element.click()
    time.sleep(1)



def two_factor(driver):
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

def file_loader(name):
    src_path = 'C:\\Users\\Vince\\Downloads'
    dst_path = 'C:\\Users\\Vince\\Desktop\\All_cals\\temp_r'
    folder_name = name.strip()
    path = os.path.join(dst_path, folder_name)
    os.mkdir(path)

    # find out about nameing conventions
    for f in os.listdir(src_path):
        n = path + "\\"+f.strip()
        o = src_path + '\\'+f.strip()
        os.rename(o,n)
    time.sleep(2)
    
def csv_reader():
    emp_names = []
    file = open('ee_roster_cals.csv')
    c = file.readlines()

    for k in c:
        i = k.strip()
        new = i[:-1]
        full = new.rpartition(',')[2]+' '+new.rpartition(',')[0]
        full = full.strip()
        emp_names.append(full)
    return emp_names

def progress_bar(emp_names,driver):
    widgets = [' [',
         progressbar.Timer(format= 'elapsed time: %(elapsed)s'),
         '] ',
           progressbar.Bar('*'),' (',
           progressbar.ETA(), ') ',
          ]
  
    bar = progressbar.ProgressBar(max_value=len(emp_names), 
                              widgets=widgets).start()
    i=0
    
    for emp_name in emp_names:
        get_docs(emp_name,driver)
        i = i+1
        bar.update(i)       
    
    
main()