import time
def b2u6(driver):
    driver.find_element_by_css_selector( '#ctl00_ContentPlaceHolder1_CourseTestTask1_dgTestTask_ctl09_Action > span > input[type="button"]').click()
    time.sleep(5)
    # 1-5
    driver.find_element_by_id('rdF4D4E67C8E674C598C1FA8243D20CE1D_1_1').click()
    driver.find_element_by_id('rd5E8B41DC51FC4BBD89EB4768B8784529_1_4').click()
    driver.find_element_by_id('rd044386A48D25423482E395BB35089019_1_2').click()
    driver.find_element_by_id('rd6C76540F1EA14E0A8869F0AB839BE880_1_3').click()
    driver.find_element_by_id('rdB996E66A0B484D5D83300466428BCBDE_1_2').click()
    # #6-15
    driver.find_element_by_id('txt_AFA4D5CCEACD4253AA49AE2670CCE1F5_1').send_keys('stayed around as a drop-in')
    driver.find_element_by_id('txt_AFA4D5CCEACD4253AA49AE2670CCE1F5_2').send_keys('expensive')
    driver.find_element_by_id('txt_AFA4D5CCEACD4253AA49AE2670CCE1F5_3').send_keys('savings')
    driver.find_element_by_id('txt_AFA4D5CCEACD4253AA49AE2670CCE1F5_4').send_keys('value')
    driver.find_element_by_id('txt_AFA4D5CCEACD4253AA49AE2670CCE1F5_5').send_keys('no idea')
    driver.find_element_by_id('txt_AFA4D5CCEACD4253AA49AE2670CCE1F5_6').send_keys('figure it out')
    driver.find_element_by_id('txt_AFA4D5CCEACD4253AA49AE2670CCE1F5_7').send_keys('looking back')
    driver.find_element_by_id('txt_AFA4D5CCEACD4253AA49AE2670CCE1F5_8').send_keys('dropping in on')
    driver.find_element_by_id('txt_AFA4D5CCEACD4253AA49AE2670CCE1F5_9').send_keys('returned')
    driver.find_element_by_id('txt_AFA4D5CCEACD4253AA49AE2670CCE1F5_10').send_keys('following my curiosity and intuition')

    # #16 -20
    driver.find_element_by_id('rdE132FC71C6A841648BFA54A4E91EF2B9_1_2').click()
    driver.find_element_by_id('rdE132FC71C6A841648BFA54A4E91EF2B9_2_2').click()
    driver.find_element_by_id('rdE132FC71C6A841648BFA54A4E91EF2B9_3_1').click()
    driver.find_element_by_id('rdE132FC71C6A841648BFA54A4E91EF2B9_4_1').click()
    driver.find_element_by_id('rdE132FC71C6A841648BFA54A4E91EF2B9_5_1').click()
    # 21 -30

    driver.find_element_by_id('txt_F4477492A5EE46C5B223FCB4911DCF86_1').send_keys('ace')
    driver.find_element_by_id('txt_F4477492A5EE46C5B223FCB4911DCF86_2').send_keys('impress')
    driver.find_element_by_id('txt_F4477492A5EE46C5B223FCB4911DCF86_3').send_keys('in conservative clothing')
    driver.find_element_by_id('txt_F4477492A5EE46C5B223FCB4911DCF86_4').send_keys('business')
    driver.find_element_by_id('txt_F4477492A5EE46C5B223FCB4911DCF86_5').send_keys('greet')
    driver.find_element_by_id('txt_F4477492A5EE46C5B223FCB4911DCF86_6').send_keys('remain as calm as possible')
    driver.find_element_by_id('txt_F4477492A5EE46C5B223FCB4911DCF86_7').send_keys('frame your responses')
    driver.find_element_by_id('txt_F4477492A5EE46C5B223FCB4911DCF86_8').send_keys('interested in')
    driver.find_element_by_id('txt_F4477492A5EE46C5B223FCB4911DCF86_9').send_keys('That way')
    driver.find_element_by_id('txt_F4477492A5EE46C5B223FCB4911DCF86_10').send_keys('follow up calls')

    time.sleep(4)

    driver.find_element_by_css_selector('#btnBottomSubmit').click()
    time.sleep(4)

    driver.switch_to_alert().accept()
    driver.refresh()
    return driver