import time

def b2u2(driver):
    driver.find_element_by_css_selector('#ctl00_ContentPlaceHolder1_CourseTestTask1_dgTestTask_ctl19_PAGER > div > ul > li.enablepage > a').click()
    driver.find_element_by_css_selector(' #ctl00_ContentPlaceHolder1_CourseTestTask1_dgTestTask_ctl07_Action > span > input[type="button"]').click()
    time.sleep(5)
    # 1-5

    driver.find_element_by_id('rd086F3077DFE642B0AF54BE7C8B3A7166_1_2').click()
    driver.find_element_by_id('rd7B719A950F304DA0B020D0EDE02CD986_1_1').click()
    driver.find_element_by_id('rdEA7CB90B2DF94B1A9D17BEFB6724C271_1_2').click()
    driver.find_element_by_id('rd13B1F4913D0F410798B44EA278BA3D76_1_4').click()
    driver.find_element_by_id('rd95AF59E1A7604862BEC5B16BD8A98A8B_1_3').click()
    # #6-15
    driver.find_element_by_id('txt_92CDCEE645DA47CD82CA1E884CDB26B6_1').send_keys('rule of thumb')
    driver.find_element_by_id('txt_92CDCEE645DA47CD82CA1E884CDB26B6_2').send_keys('delicacies')
    driver.find_element_by_id('txt_92CDCEE645DA47CD82CA1E884CDB26B6_3').send_keys('edible')
    driver.find_element_by_id('txt_92CDCEE645DA47CD82CA1E884CDB26B6_4').send_keys('century egg')
    driver.find_element_by_id('txt_92CDCEE645DA47CD82CA1E884CDB26B6_5').send_keys('brown')
    driver.find_element_by_id('txt_92CDCEE645DA47CD82CA1E884CDB26B6_6').send_keys('bird\' s nest')
    driver.find_element_by_id('txt_92CDCEE645DA47CD82CA1E884CDB26B6_7').send_keys('distinctive')
    driver.find_element_by_id('txt_92CDCEE645DA47CD82CA1E884CDB26B6_8').send_keys('drunken shrimp')
    driver.find_element_by_id('txt_92CDCEE645DA47CD82CA1E884CDB26B6_9').send_keys('taste bad')
    driver.find_element_by_id('txt_92CDCEE645DA47CD82CA1E884CDB26B6_10').send_keys('made my soul feel bad')

    # 16 -25
    driver.find_element_by_id('rd97851D6C0AD44D558FA16BEBB2A26E4B_1_2').click()
    driver.find_element_by_id('rd97851D6C0AD44D558FA16BEBB2A26E4B_2_2').click()
    driver.find_element_by_id('rd97851D6C0AD44D558FA16BEBB2A26E4B_3_1').click()
    driver.find_element_by_id('rd97851D6C0AD44D558FA16BEBB2A26E4B_4_2').click()
    driver.find_element_by_id('rd97851D6C0AD44D558FA16BEBB2A26E4B_5_1').click()

    driver.find_element_by_id('txt_9C053CB9C85D43BEA188BEDF56A083D8_1').send_keys('bacon')
    driver.find_element_by_id('txt_9C053CB9C85D43BEA188BEDF56A083D8_2').send_keys('fried bread')
    driver.find_element_by_id('txt_9C053CB9C85D43BEA188BEDF56A083D8_3').send_keys('mushrooms')
    driver.find_element_by_id('txt_9C053CB9C85D43BEA188BEDF56A083D8_4').send_keys('Sandwich')
    driver.find_element_by_id('txt_9C053CB9C85D43BEA188BEDF56A083D8_5').send_keys('a piece of fruit')
    driver.find_element_by_id('txt_9C053CB9C85D43BEA188BEDF56A083D8_6').send_keys('vegetables')
    driver.find_element_by_id('txt_9C053CB9C85D43BEA188BEDF56A083D8_7').send_keys('meat')
    driver.find_element_by_id('txt_9C053CB9C85D43BEA188BEDF56A083D8_8').send_keys('pasta')
    driver.find_element_by_id('txt_9C053CB9C85D43BEA188BEDF56A083D8_9').send_keys('carrots')
    driver.find_element_by_id('txt_9C053CB9C85D43BEA188BEDF56A083D8_10').send_keys('cabbages')

    time.sleep(4)

    driver.find_element_by_css_selector('#btnBottomSubmit').click()
    time.sleep(4)

    driver.switch_to_alert().accept()
    driver.refresh()
    return driver