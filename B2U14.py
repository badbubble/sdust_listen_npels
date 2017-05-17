import time

def b2u14(driver):
    #driver.find_element_by_css_selector('#ctl00_ContentPlaceHolder1_CourseTestTask1_dgTestTask_ctl19_PAGER > div > ul > li.enablepage > a').click()
    driver.find_element_by_css_selector('#ctl00_ContentPlaceHolder1_CourseTestTask1_dgTestTask_ctl11_Action > span > input[type="button"]').click()
    time.sleep(5)
    # 1-5
    driver.find_element_by_id('rd328FDDEB79204F2B98D52214B96A546C_1_2').click()
    driver.find_element_by_id('rd31782210F8AA4D8EB28EC811BFCFA997_1_4').click()
    driver.find_element_by_id('rdA067F640830D4908AF8964D026238205_1_3').click()
    driver.find_element_by_id('rd1DE2EC8D41C244F7BD39F2930E3E2CB1_1_1').click()
    driver.find_element_by_id('rd5B7AAB3899944E7F8E1A5A9955DBD0C4_1_1').click()

    # #6-15
    driver.find_element_by_id('txt_E600404AF8BD42A19FDADFC4B48D44F2_1').send_keys('British')
    driver.find_element_by_id('txt_E600404AF8BD42A19FDADFC4B48D44F2_2').send_keys('lazy drunks')
    driver.find_element_by_id('txt_E600404AF8BD42A19FDADFC4B48D44F2_3').send_keys('A wave of')
    driver.find_element_by_id('txt_E600404AF8BD42A19FDADFC4B48D44F2_4').send_keys('assimilate')
    driver.find_element_by_id('txt_E600404AF8BD42A19FDADFC4B48D44F2_5').send_keys('critics')
    driver.find_element_by_id('txt_E600404AF8BD42A19FDADFC4B48D44F2_6').send_keys('integral')
    driver.find_element_by_id('txt_E600404AF8BD42A19FDADFC4B48D44F2_7').send_keys('productive capacity')
    driver.find_element_by_id('txt_E600404AF8BD42A19FDADFC4B48D44F2_8').send_keys('economic edge')
    driver.find_element_by_id('txt_E600404AF8BD42A19FDADFC4B48D44F2_9').send_keys('trade and invest')
    driver.find_element_by_id('txt_E600404AF8BD42A19FDADFC4B48D44F2_10').send_keys('flexible')

    driver.find_element_by_id('rdA153919BE7EA45B7ACA1109BC715F649_1_1').click()
    driver.find_element_by_id('rdA153919BE7EA45B7ACA1109BC715F649_2_2').click()
    driver.find_element_by_id('rdA153919BE7EA45B7ACA1109BC715F649_3_1').click()
    driver.find_element_by_id('rdA153919BE7EA45B7ACA1109BC715F649_4_2').click()
    driver.find_element_by_id('rdA153919BE7EA45B7ACA1109BC715F649_5_1').click()
    # 16 -25

    driver.find_element_by_id('txt_41A779AFC2AA41959D89EBA50D2E8262_1').send_keys('disturbance')
    driver.find_element_by_id('txt_41A779AFC2AA41959D89EBA50D2E8262_2').send_keys('cultural background')
    driver.find_element_by_id('txt_41A779AFC2AA41959D89EBA50D2E8262_3').send_keys('rather than')
    driver.find_element_by_id('txt_41A779AFC2AA41959D89EBA50D2E8262_4').send_keys('disappear')
    driver.find_element_by_id('txt_41A779AFC2AA41959D89EBA50D2E8262_5').send_keys('get over')
    driver.find_element_by_id('txt_41A779AFC2AA41959D89EBA50D2E8262_6').send_keys('symbol system')
    driver.find_element_by_id('txt_41A779AFC2AA41959D89EBA50D2E8262_7').send_keys('adults')
    driver.find_element_by_id('txt_41A779AFC2AA41959D89EBA50D2E8262_8').send_keys('no matter how')
    driver.find_element_by_id('txt_41A779AFC2AA41959D89EBA50D2E8262_9').send_keys('gain confidence')
    driver.find_element_by_id('txt_41A779AFC2AA41959D89EBA50D2E8262_10').send_keys('open up')

    time.sleep(4)

    driver.find_element_by_css_selector('#btnBottomSubmit').click()
    time.sleep(4)

    driver.switch_to_alert().accept()
    driver.refresh()
    return driver