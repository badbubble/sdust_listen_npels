import time

def b2u5(driver):
    #driver.find_element_by_css_selector('#ctl00_ContentPlaceHolder1_CourseTestTask1_dgTestTask_ctl19_PAGER > div > ul > li.enablepage > a').click()
    driver.find_element_by_css_selector('#ctl00_ContentPlaceHolder1_CourseTestTask1_dgTestTask_ctl10_Action > span > input[type="button"]').click()
    time.sleep(5)
    # 1-5
    driver.find_element_by_id('rd5E6528E677C94F87AC847AAAEB52FC15_1_1').click()
    driver.find_element_by_id('rd00C3224A992E4D19A23E9D52F9D5D11E_1_3').click()
    driver.find_element_by_id('rdD258C0F2A06C40039538069B1A776BCF_1_2').click()
    driver.find_element_by_id('rd301F26273AD74D00AA384C4ABE5B2271_1_1').click()
    driver.find_element_by_id('rd63FF44692C5D428F8EBDC8F15EDDBFE2_1_4').click()

    # #6-15
    driver.find_element_by_id('txt_0F869153BB4A4D01BD88591D697438ED_1').send_keys('trouble')
    driver.find_element_by_id('txt_0F869153BB4A4D01BD88591D697438ED_2').send_keys('out of breath')
    driver.find_element_by_id('txt_0F869153BB4A4D01BD88591D697438ED_3').send_keys('How long')
    driver.find_element_by_id('txt_0F869153BB4A4D01BD88591D697438ED_4').send_keys('appetite')
    driver.find_element_by_id('txt_0F869153BB4A4D01BD88591D697438ED_5').send_keys('stress')
    driver.find_element_by_id('txt_0F869153BB4A4D01BD88591D697438ED_6').send_keys('responsible for it')
    driver.find_element_by_id('txt_0F869153BB4A4D01BD88591D697438ED_7').send_keys('examine')
    driver.find_element_by_id('txt_0F869153BB4A4D01BD88591D697438ED_8').send_keys('works')
    driver.find_element_by_id('txt_0F869153BB4A4D01BD88591D697438ED_9').send_keys('Relax')
    driver.find_element_by_id('txt_0F869153BB4A4D01BD88591D697438ED_10').send_keys('recommend')

    driver.find_element_by_id('rdB7B7FA0F123D4CE7AF090ADE0275AC57_1_1').click()
    driver.find_element_by_id('rdB7B7FA0F123D4CE7AF090ADE0275AC57_2_2').click()
    driver.find_element_by_id('rdB7B7FA0F123D4CE7AF090ADE0275AC57_3_2').click()
    driver.find_element_by_id('rdB7B7FA0F123D4CE7AF090ADE0275AC57_4_2').click()
    driver.find_element_by_id('rdB7B7FA0F123D4CE7AF090ADE0275AC57_5_1').click()
    # 16 -25

    driver.find_element_by_id('txt_47DD3ACA9F044998A126DEA79E1AEA6D_1').send_keys('golden rule')
    driver.find_element_by_id('txt_47DD3ACA9F044998A126DEA79E1AEA6D_2').send_keys('gradual progression')
    driver.find_element_by_id('txt_47DD3ACA9F044998A126DEA79E1AEA6D_3').send_keys('build up')
    driver.find_element_by_id('txt_47DD3ACA9F044998A126DEA79E1AEA6D_4').send_keys('sustainable')
    driver.find_element_by_id('txt_47DD3ACA9F044998A126DEA79E1AEA6D_5').send_keys('engage in')
    driver.find_element_by_id('txt_47DD3ACA9F044998A126DEA79E1AEA6D_6').send_keys('human movement')
    driver.find_element_by_id('txt_47DD3ACA9F044998A126DEA79E1AEA6D_7').send_keys('supportive shoes')
    driver.find_element_by_id('txt_47DD3ACA9F044998A126DEA79E1AEA6D_8').send_keys('up to you')
    driver.find_element_by_id('txt_47DD3ACA9F044998A126DEA79E1AEA6D_9').send_keys('consecutive')
    driver.find_element_by_id('txt_47DD3ACA9F044998A126DEA79E1AEA6D_10').send_keys('divide')

    time.sleep(4)

    driver.find_element_by_css_selector('#btnBottomSubmit').click()
    time.sleep(4)

    driver.switch_to_alert().accept()
    driver.refresh()
    return driver