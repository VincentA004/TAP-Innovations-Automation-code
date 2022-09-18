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
        file = open("index_log_EI9.txt", "w")
        #driver = webdriver.Chrome("chromedriver.exe")
        options = webdriver.ChromeOptions()
        #options.add_argument('--user-data-dir=C:\\Users\\Vince\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1')
        driver = uc.Chrome(version_main = 103 , options = options)
        driver.maximize_window()
        driver.get('https://smartcompliance.adp.com/avs/launchapp/#/workspaces/employment-tax//processes')
        u = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID,"login-form_username")))
        u.send_keys(username,Keys.RETURN)
        p = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"login-form_password")))
        p.send_keys(password,Keys.RETURN)
        two_factor()
        time.sleep(10)
        url_E9 = 'https://workforcenow.adp.com/theme/admin.html#/Process_ttd_EI9Management/EI9Management'
        # null number = 2019288173011FA
        time.sleep(5)
        py.hotkey('ctrl', 't')
        time.sleep(.1)
        py.write(url_E9)
        py.press('enter')
        time.sleep(25)
        py.click(x = 850 , y=780, clicks = 1 ) #closed box
        #py.click(x=1326,y=792,clicks=1)
        time.sleep(3)
        file2 = open('caseId_E-I9-2.txt')
        case_num = file2.readlines()
        time.sleep(4)
        progress_bar(case_num,file)
            

#figure out phantom lag


def document_downloader(c,file):
    time.sleep(4)
    py.doubleClick(x=2220 , y=940)
    py.press('delete')
    time.sleep(.1)
    py.write(c)
    py.press('enter')
    time.sleep(2)
    #py.click(x=541,y=1150, clicks = 1) # person link name
    py.click(x = 515 , y=1150, clicks = 1) # person link name-variety 2
    time.sleep(2)
    name = selector(783,315,1500,315)
    py.sleep(2)
    py.click(x=1840,y=550, clicks = 1) #documents tab
    time.sleep(2)
    py.click(x=2470,y=755,clicks = 1) #doc 1
    time.sleep(2)
    py.click(x=2470,y=905,clicks=1) #doc 2
    time.sleep(2)
    py.click(x=2470,y=1025, clicks =1) #doc 3
    time.sleep(2)
    py.click(x=2470,y=1135, clicks =1) #doc 4
    time.sleep(2)
    py.click(x=2470,y=1256, clicks =1) #doc 5
    time.sleep(1)
    py.click(x=2470,y=1369, clicks =1) #doc 6
    time.sleep(2)
    py.click(x=613,y=327, clicks = 1) # multiple downloads button
    time.sleep(1)
    py.click(x=613, y=400 , clicks = 1) #off click
    time.sleep(1)
    file_loader(name,c)
    time.sleep(1)
    index_file(c,name,file)
    time.sleep(1)
    
    
    
def selector(a,b,c,d):
    py.moveTo(a, b)
    py.mouseDown(button='left')
    py.moveTo(c, d, 1)
    time.sleep(1)
    text = copy_clipboard()
    return text

def copy_clipboard():
    root = Tk()     
    root.withdraw() 
    pc.copy('null')
    time.sleep(.1)
    py.hotkey("ctrl", "c") 
    time.sleep(.1)
    clipboard = root.clipboard_get()
    #ans: try catch- figure out
    #try:
    #    clipboard = root.clipboard_get()
    #except:
    #    clipboard='null'
    return clipboard
    
def file_loader(name,c):
    src_path = 'C:\\Users\\Vince\\Downloads'
    dst_path = 'C:\\Users\\Vince\\Desktop\\temp_x\\'
    folder_name = name.strip()+'_'+c.strip()
    path = os.path.join(dst_path, folder_name)
    os.mkdir(path)

    # find out about nameing conventions
    for f in os.listdir(src_path):
        n = path + "\\"+f.strip()
        o = src_path + '\\'+f.strip()
        os.rename(o,n)
    
def index_file(c,n,file):
    str = n.strip()+'_'+c.strip()
    file.write(str+"\n")

def two_factor():
    username = u2
    password = p2
    outlook_link = 'https://outlook.office.com/mail/'
    time.sleep(3)
    py.click(x=1637,y=727,clicks = 1)
    time.sleep(1)
    py.hotkey('ctrl', 't')
    time.sleep(.5)
    py.write(outlook_link)
    py.press('enter')
    time.sleep(7)
    py.write(username)
    py.press('enter')
    time.sleep(3.5)
    py.write(password)
    py.press('enter')
    time.sleep(2)
    py.press('enter')
    time.sleep(9)
    py.click(x=867,y=491,clicks=1)
    time.sleep(7)
    code = selector(2050,1125,2284,1125)
    time.sleep(1)
    py.hotkey('ctrl', 'w')
    time.sleep(3)
    py.write(code)
    py.press('enter')
    time.sleep(2.5)

def progress_bar(case_num,file):
    widgets = [' [',
         progressbar.Timer(format= 'elapsed time: %(elapsed)s'),
         '] ',
           progressbar.Bar('*'),' (',
           progressbar.ETA(), ') ',
          ]
  
    bar = progressbar.ProgressBar(max_value=len(case_num), 
                              widgets=widgets).start()
    i=0
    for(n) in case_num:
        time.sleep(1)
        document_downloader(n.strip(),file)
        i = i+1
        bar.update(i)

    
    
    
main()