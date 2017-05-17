import time
def b2u9(driver):
    driver.find_element_by_css_selector( '#ctl00_ContentPlaceHolder1_CourseTestTask1_dgTestTask_ctl06_Action > span:nth-child(1) > input:nth-child(1)').click()
    time.sleep(5)
    # 1-5
    driver.find_element_by_id('rd5FC50288459F45BEAAEEB2E8AEDB5ED1_1_1').click()
    driver.find_element_by_id('rd826F089CC98E4AC282A2D02B3B4B2A6D_1_3').click()
    driver.find_element_by_id('rd16422F97F6014E3CB0532D63B44C1CDD_1_4').click()
    driver.find_element_by_id('rd5103D95ED6AF41438227DB0C590808A2_1_3').click()
    driver.find_element_by_id('rdEFBAE4A76E9148C989B57733477C96E1_1_4').click()
    # #6-15
    driver.find_element_by_id('txt_D2302878C8434CD68F854DED172DB8EA_1').send_keys('unique')
    driver.find_element_by_id('txt_D2302878C8434CD68F854DED172DB8EA_2').send_keys('the quality of your life')
    driver.find_element_by_id('txt_D2302878C8434CD68F854DED172DB8EA_3').send_keys('whatever it is')
    driver.find_element_by_id('txt_D2302878C8434CD68F854DED172DB8EA_4').send_keys('education')
    driver.find_element_by_id('txt_D2302878C8434CD68F854DED172DB8EA_5').send_keys('career')
    driver.find_element_by_id('txt_D2302878C8434CD68F854DED172DB8EA_6').send_keys('portion')
    driver.find_element_by_id('txt_D2302878C8434CD68F854DED172DB8EA_7').send_keys('acquire')
    driver.find_element_by_id('txt_D2302878C8434CD68F854DED172DB8EA_8').send_keys('pursuit')
    driver.find_element_by_id('txt_D2302878C8434CD68F854DED172DB8EA_9').send_keys('define')
    driver.find_element_by_id('txt_D2302878C8434CD68F854DED172DB8EA_10').send_keys('regret')

    # #16 -20
    driver.find_element_by_id('rdFB05F4C98E1643E793D5AD72668CA817_1_1').click()
    driver.find_element_by_id('rdFB05F4C98E1643E793D5AD72668CA817_2_1').click()
    driver.find_element_by_id('rdFB05F4C98E1643E793D5AD72668CA817_3_1').click()
    driver.find_element_by_id('rdFB05F4C98E1643E793D5AD72668CA817_4_1').click()
    driver.find_element_by_id('rdFB05F4C98E1643E793D5AD72668CA817_5_2').click()
    # 21 -30

    driver.find_element_by_id('txt_8EDF19D4566D48CDA35FB2386E8259EE_1').send_keys('decay')
    driver.find_element_by_id('txt_8EDF19D4566D48CDA35FB2386E8259EE_2').send_keys('direction')
    driver.find_element_by_id('txt_8EDF19D4566D48CDA35FB2386E8259EE_3').send_keys('false belief')
    driver.find_element_by_id('txt_8EDF19D4566D48CDA35FB2386E8259EE_4').send_keys('greater than')
    driver.find_element_by_id('txt_8EDF19D4566D48CDA35FB2386E8259EE_5').send_keys('weaknesses')
    driver.find_element_by_id('txt_8EDF19D4566D48CDA35FB2386E8259EE_6').send_keys('disgust')
    driver.find_element_by_id('txt_8EDF19D4566D48CDA35FB2386E8259EE_7').send_keys('poverty')
    driver.find_element_by_id('txt_8EDF19D4566D48CDA35FB2386E8259EE_8').send_keys('get used to')
    driver.find_element_by_id('txt_8EDF19D4566D48CDA35FB2386E8259EE_9').send_keys('motivation')
    driver.find_element_by_id('txt_8EDF19D4566D48CDA35FB2386E8259EE_10').send_keys('personal goals')

    time.sleep(4)

    driver.find_element_by_css_selector('#btnBottomSubmit').click()
    driver.find_element_by_css_selector('#btnBottomSubmit').click()
    time.sleep(4)

    driver.switch_to_alert().accept()
    driver.refresh()
    return driver