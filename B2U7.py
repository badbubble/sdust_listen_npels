import time
def b2u7(driver):
    driver.find_element_by_css_selector( '#ctl00_ContentPlaceHolder1_CourseTestTask1_dgTestTask_ctl08_Action > span > input[type="button"]').click()
    time.sleep(5)
    # 1-5
    driver.find_element_by_id('rdE09245BC314E438C844F7EAFA3C01E4F_1_3').click()
    driver.find_element_by_id('rd1D402E1CC7E648F782669F1EB0CC447B_1_1').click()
    driver.find_element_by_id('rd60A2DE6A4CBA4E83A4EF93C03C97DB1C_1_2').click()
    driver.find_element_by_id('rdD7E6F958B88D4B8BBF33D13A01511F82_1_4').click()
    driver.find_element_by_id('rd2AF090201F9A44EDB0E32BFA1AFE272C_1_3').click()
    # #6-15
    driver.find_element_by_id('txt_E1AC4131D30A4BC693816BEB0E6F5BA6_1').send_keys('scarves')
    driver.find_element_by_id('txt_E1AC4131D30A4BC693816BEB0E6F5BA6_2').send_keys('silk')
    driver.find_element_by_id('txt_E1AC4131D30A4BC693816BEB0E6F5BA6_3').send_keys('nice')
    driver.find_element_by_id('txt_E1AC4131D30A4BC693816BEB0E6F5BA6_4').send_keys('winter')
    driver.find_element_by_id('txt_E1AC4131D30A4BC693816BEB0E6F5BA6_5').send_keys('wool scarf')
    driver.find_element_by_id('txt_E1AC4131D30A4BC693816BEB0E6F5BA6_6').send_keys('seventy-five dollars')
    driver.find_element_by_id('txt_E1AC4131D30A4BC693816BEB0E6F5BA6_7').send_keys('tax')
    driver.find_element_by_id('txt_E1AC4131D30A4BC693816BEB0E6F5BA6_8').send_keys('10 percent')
    driver.find_element_by_id('txt_E1AC4131D30A4BC693816BEB0E6F5BA6_9').send_keys('wrap')
    driver.find_element_by_id('txt_E1AC4131D30A4BC693816BEB0E6F5BA6_10').send_keys('up')
    # #16 -20
    driver.find_element_by_id('rdC2B5F0FB24A944C79ED04972E949ECD3_1_2').click()
    driver.find_element_by_id('rdC2B5F0FB24A944C79ED04972E949ECD3_2_2').click()
    driver.find_element_by_id('rdC2B5F0FB24A944C79ED04972E949ECD3_3_1').click()
    driver.find_element_by_id('rdC2B5F0FB24A944C79ED04972E949ECD3_4_1').click()
    driver.find_element_by_id('rdC2B5F0FB24A944C79ED04972E949ECD3_5_1').click()
    # 21 -30

    driver.find_element_by_id('txt_ECCACD66623643B5A14B9A17F1847C68_1').send_keys('wouldn\'t buy')
    driver.find_element_by_id('txt_ECCACD66623643B5A14B9A17F1847C68_2').send_keys('starters')
    driver.find_element_by_id('txt_ECCACD66623643B5A14B9A17F1847C68_3').send_keys('labels')
    driver.find_element_by_id('txt_ECCACD66623643B5A14B9A17F1847C68_4').send_keys('style')
    driver.find_element_by_id('txt_ECCACD66623643B5A14B9A17F1847C68_5').send_keys('missing')
    driver.find_element_by_id('txt_ECCACD66623643B5A14B9A17F1847C68_6').send_keys('brands')
    driver.find_element_by_id('txt_ECCACD66623643B5A14B9A17F1847C68_7').send_keys('trendy')
    driver.find_element_by_id('txt_ECCACD66623643B5A14B9A17F1847C68_8').send_keys('figure out')
    driver.find_element_by_id('txt_ECCACD66623643B5A14B9A17F1847C68_9').send_keys('handbag')
    driver.find_element_by_id('txt_ECCACD66623643B5A14B9A17F1847C68_10').send_keys('point you to what\'s hot')

    time.sleep(4)

    driver.find_element_by_css_selector('#btnBottomSubmit').click()
    time.sleep(4)

    driver.switch_to_alert().accept()
    driver.refresh()
    return driver