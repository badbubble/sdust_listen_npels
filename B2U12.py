import time
def b2u12(driver):
    driver.find_element_by_css_selector( '#ctl00_ContentPlaceHolder1_CourseTestTask1_dgTestTask_ctl13_Action > span > input[type="button"]').click()
    time.sleep(5)
    # 1-5
    driver.find_element_by_id('rdF3B669259EF546279FAF375B35CE09EA_1_4').click()
    driver.find_element_by_id('rdC95C41D102CA4348852B464944DAE9C0_1_4').click()
    driver.find_element_by_id('rd0B3CFB0BA60B4C029CDF43C5DC570224_1_3').click()
    driver.find_element_by_id('rd6B11BD7B0D5149E99DF1AEFC4E354E38_1_1').click()
    driver.find_element_by_id('rd67D843C26E344ADDB5D8DC8063869F04_1_4').click()
    # #6-15
    driver.find_element_by_id('txt_57EE95BD2A30449CB059101679F3E01B_1').send_keys('social interaction')
    driver.find_element_by_id('txt_57EE95BD2A30449CB059101679F3E01B_2').send_keys('usability')
    driver.find_element_by_id('txt_57EE95BD2A30449CB059101679F3E01B_3').send_keys('websites')
    driver.find_element_by_id('txt_57EE95BD2A30449CB059101679F3E01B_4').send_keys('a wide variety of')
    driver.find_element_by_id('txt_57EE95BD2A30449CB059101679F3E01B_5').send_keys('connect with')
    driver.find_element_by_id('txt_57EE95BD2A30449CB059101679F3E01B_6').send_keys('acquaintances')
    driver.find_element_by_id('txt_57EE95BD2A30449CB059101679F3E01B_7').send_keys('book vacations')
    driver.find_element_by_id('txt_57EE95BD2A30449CB059101679F3E01B_8').send_keys('has seen')
    driver.find_element_by_id('txt_57EE95BD2A30449CB059101679F3E01B_9').send_keys('desktops')
    driver.find_element_by_id('txt_57EE95BD2A30449CB059101679F3E01B_10').send_keys('settings')

    # #16 -20
    driver.find_element_by_id('rd10F252D65C424776B6201F19B9A5FFC8_1_2').click()
    driver.find_element_by_id('rd10F252D65C424776B6201F19B9A5FFC8_2_1').click()
    driver.find_element_by_id('rd10F252D65C424776B6201F19B9A5FFC8_3_2').click()
    driver.find_element_by_id('rd10F252D65C424776B6201F19B9A5FFC8_4_1').click()
    driver.find_element_by_id('rd10F252D65C424776B6201F19B9A5FFC8_5_2').click()
    # 21 -30

    driver.find_element_by_id('txt_CECCCCCF8949461288E1BA1FF12D9F3C_1').send_keys('analyzed the relationships')
    driver.find_element_by_id('txt_CECCCCCF8949461288E1BA1FF12D9F3C_2').send_keys('search engine')
    driver.find_element_by_id('txt_CECCCCCF8949461288E1BA1FF12D9F3C_3').send_keys('domain name')
    driver.find_element_by_id('txt_CECCCCCF8949461288E1BA1FF12D9F3C_4').send_keys('September 4, 1998')
    driver.find_element_by_id('txt_CECCCCCF8949461288E1BA1FF12D9F3C_5').send_keys('garage')
    driver.find_element_by_id('txt_CECCCCCF8949461288E1BA1FF12D9F3C_6').send_keys('fellow')
    driver.find_element_by_id('txt_CECCCCCF8949461288E1BA1FF12D9F3C_7').send_keys('the first employee')
    driver.find_element_by_id('txt_CECCCCCF8949461288E1BA1FF12D9F3C_8').send_keys(' 1 billion')
    driver.find_element_by_id('txt_CECCCCCF8949461288E1BA1FF12D9F3C_9').send_keys('8.4 percent')
    driver.find_element_by_id('txt_CECCCCCF8949461288E1BA1FF12D9F3C_10').send_keys('931 million')

    time.sleep(4)

    driver.find_element_by_css_selector('#btnBottomSubmit').click()
    time.sleep(4)

    driver.switch_to_alert().accept()
    driver.refresh()
    return driver