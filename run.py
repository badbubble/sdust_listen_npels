from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import B2U1,B2U9,B2U3,B2U10,B2U12,B2U13,B2U2,B2U11,B2U6,B2U5,B2U8,B2U14,B2U4,B2U7,B2U132
username ='201601061316' #input('请输入账号>>')
pwd ='lhj980205' #input('请输入密码>>')
npelsurl = 'http://192.168.100.117/NPELS'
driver = webdriver.Chrome()
driver.get(npelsurl)
driver.find_element_by_id("tbName").send_keys(username)
driver.find_element_by_id("tbPwd").send_keys(pwd)
driver.find_element_by_id('btnLogin').click()
time.sleep(5)
driver.switch_to.frame('mainFrame')
driver.find_element_by_css_selector( '#ctl00_cphContent_divWarning > div > div.homework_3 > ul > li.homework_3_1 > a').click()
time.sleep(4)
while(True):
    chos = input('输入听力单元数>>')
    if(chos == 'exit'):
        print('感谢使用')
        break
    if(int(chos) == 1):
        B2U1.b2u1(driver)
    if (int(chos) == 2):
        B2U2.b2u2(driver)
    if (int(chos) == 3):
        B2U3.b2u3(driver)
    if (int(chos) == 4):
        B2U4.b2u4(driver)
    if (int(chos) == 5):
        B2U5.b2u5(driver)
    if (int(chos) == 6):
        B2U6.b2u6(driver)
    if (int(chos) == 7):
        B2U7.b2u7(driver)
    if (int(chos) == 8):
        B2U8.b2u8(driver)
    if (int(chos) == 9):
        B2U9.b2u9(driver)
    if (int(chos) == 10):
         B2U10.b2u10(driver)
    if (int(chos) == 11):
        B2U11.b2u11(driver)
    if (int(chos) == 12):
        B2U12.b2u12(driver)
    if (int(chos) == 13):
        B2U13.b2u13(driver)
    if (int(chos) == 14):
        B2U14.b2u14(driver)
    if (int(chos) == 132):
        B2U132.b2u132(driver)
    time.sleep(2)
    driver.switch_to.frame('mainFrame')
    driver.find_element_by_css_selector('#ctl00_cphContent_divWarning > div > div.homework_3 > ul > li.homework_3_1 > a').click()

driver.close()




