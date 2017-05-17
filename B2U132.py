import time

def b2u132(driver):
    driver.find_element_by_css_selector('#ctl00_ContentPlaceHolder1_CourseTestTask1_dgTestTask_ctl19_PAGER > div > ul > li.enablepage > a').click()
    driver.find_element_by_css_selector('#ctl00_ContentPlaceHolder1_CourseTestTask1_dgTestTask_ctl08_Action > span > input[type="button"]').click()
    time.sleep(5)
    # 1-5

    driver.find_element_by_id('rd49BCFEE583E34CC2907CA97FBBE8C7BE_1_2').click()
    driver.find_element_by_id('rd9FF417D9320D4B419703B0C68EB6BB1B_1_1').click()
    driver.find_element_by_id('rd7CE90B2556CA45E381F42277B7B90DD7_1_3').click()
    driver.find_element_by_id('rd54E71D986E20492E84EAAC819FE2906D_1_1').click()
    driver.find_element_by_id('rdB39E284DFF49447BA53B2F3D0D9A7A22_1_3').click()
    # #6-15
    driver.find_element_by_id('txt_4ECBA72C4A6841F1982532650A169EA7_1').send_keys('Qualities')
    driver.find_element_by_id('txt_4ECBA72C4A6841F1982532650A169EA7_2').send_keys('every detail')
    driver.find_element_by_id('txt_4ECBA72C4A6841F1982532650A169EA7_3').send_keys('intentions')
    driver.find_element_by_id('txt_4ECBA72C4A6841F1982532650A169EA7_4').send_keys('adaptable')
    driver.find_element_by_id('txt_4ECBA72C4A6841F1982532650A169EA7_5').send_keys('read your mind')
    driver.find_element_by_id('txt_4ECBA72C4A6841F1982532650A169EA7_6').send_keys('annoys')
    driver.find_element_by_id('txt_4ECBA72C4A6841F1982532650A169EA7_7').send_keys('trust')
    driver.find_element_by_id('txt_4ECBA72C4A6841F1982532650A169EA7_8').send_keys('personality')
    driver.find_element_by_id('txt_4ECBA72C4A6841F1982532650A169EA7_9').send_keys('gossip')
    driver.find_element_by_id('txt_4ECBA72C4A6841F1982532650A169EA7_10').send_keys('stick up for')

    # 16 -25
    driver.find_element_by_id('rdD6E679B05A5A4101868ADD75437082DF_1_1').click()
    driver.find_element_by_id('rdD6E679B05A5A4101868ADD75437082DF_2_1').click()
    driver.find_element_by_id('rdD6E679B05A5A4101868ADD75437082DF_3_2').click()
    driver.find_element_by_id('rdD6E679B05A5A4101868ADD75437082DF_4_1').click()
    driver.find_element_by_id('rdD6E679B05A5A4101868ADD75437082DF_5_2').click()

    driver.find_element_by_id('txt_A2CDB2AC57184E7482E944572564E707_1').send_keys('high moral standard')
    driver.find_element_by_id('txt_A2CDB2AC57184E7482E944572564E707_2').send_keys('thought and behavior')
    driver.find_element_by_id('txt_A2CDB2AC57184E7482E944572564E707_3').send_keys('examples')
    driver.find_element_by_id('txt_A2CDB2AC57184E7482E944572564E707_4').send_keys('learning')
    driver.find_element_by_id('txt_A2CDB2AC57184E7482E944572564E707_5').send_keys('acquired')
    driver.find_element_by_id('txt_A2CDB2AC57184E7482E944572564E707_6').send_keys('characteristic')
    driver.find_element_by_id('txt_A2CDB2AC57184E7482E944572564E707_7').send_keys('isolation')
    driver.find_element_by_id('txt_A2CDB2AC57184E7482E944572564E707_8').send_keys('communities')
    driver.find_element_by_id('txt_A2CDB2AC57184E7482E944572564E707_9').send_keys('including')
    driver.find_element_by_id('txt_A2CDB2AC57184E7482E944572564E707_10').send_keys('associations')

    time.sleep(4)

    driver.find_element_by_css_selector('#btnBottomSubmit').click()
    time.sleep(4)

    driver.switch_to_alert().accept()
    driver.refresh()
    return driver
