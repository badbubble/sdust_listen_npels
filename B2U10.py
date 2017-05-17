import time
def b2u10(driver):
    driver.find_element_by_css_selector( '#ctl00_ContentPlaceHolder1_CourseTestTask1_dgTestTask_ctl05_Action > span > input[type="button"]').click()
    time.sleep(5)
    # 1-5
    driver.find_element_by_id('rd2A27429185D046E19C2A962068A17DB2_1_2').click()
    driver.find_element_by_id('rd71DE2CDCEEC84EC1926F421436A13071_1_1').click()
    driver.find_element_by_id('rdC1CB3E54EB9240DCBB3C6089DB233E2C_1_3').click()
    driver.find_element_by_id('rd583A3A9C39DC43B594E93023E25B0C63_1_4').click()
    driver.find_element_by_id('rdFC59B629A5B8490887B37C0F8E88E446_1_4').click()
    # #6-15
    driver.find_element_by_id('txt_82236D58D5A94CF891C3D1982EE231C9_1').send_keys('Car crash')
    driver.find_element_by_id('txt_82236D58D5A94CF891C3D1982EE231C9_2').send_keys('On Sunday morning')
    driver.find_element_by_id('txt_82236D58D5A94CF891C3D1982EE231C9_3').send_keys('County')
    driver.find_element_by_id('txt_82236D58D5A94CF891C3D1982EE231C9_4').send_keys('Two')
    driver.find_element_by_id('txt_82236D58D5A94CF891C3D1982EE231C9_5').send_keys('State Road 24')
    driver.find_element_by_id('txt_82236D58D5A94CF891C3D1982EE231C9_6').send_keys('18')
    driver.find_element_by_id('txt_82236D58D5A94CF891C3D1982EE231C9_7').send_keys('17')
    driver.find_element_by_id('txt_82236D58D5A94CF891C3D1982EE231C9_8').send_keys('43')
    driver.find_element_by_id('txt_82236D58D5A94CF891C3D1982EE231C9_9').send_keys('Martin')
    driver.find_element_by_id('txt_82236D58D5A94CF891C3D1982EE231C9_10').send_keys('Wittig')

    # #16 -20
    driver.find_element_by_id('rd148B4AD50C2E4EF88E357691B5E922A7_1_2').click()
    driver.find_element_by_id('rd148B4AD50C2E4EF88E357691B5E922A7_2_1').click()
    driver.find_element_by_id('rd148B4AD50C2E4EF88E357691B5E922A7_3_2').click()
    driver.find_element_by_id('rd148B4AD50C2E4EF88E357691B5E922A7_4_2').click()
    driver.find_element_by_id('rd148B4AD50C2E4EF88E357691B5E922A7_5_1').click()
    # 21 -30

    driver.find_element_by_id('txt_F75E3A236075405ABC94001D5E41E3FC_1').send_keys('rare')
    driver.find_element_by_id('txt_F75E3A236075405ABC94001D5E41E3FC_2').send_keys('primary cause')
    driver.find_element_by_id('txt_F75E3A236075405ABC94001D5E41E3FC_3').send_keys('property')
    driver.find_element_by_id('txt_F75E3A236075405ABC94001D5E41E3FC_4').send_keys('objects')
    driver.find_element_by_id('txt_F75E3A236075405ABC94001D5E41E3FC_5').send_keys('skip like')
    driver.find_element_by_id('txt_F75E3A236075405ABC94001D5E41E3FC_6').send_keys('prone')
    driver.find_element_by_id('txt_F75E3A236075405ABC94001D5E41E3FC_7').send_keys('in advance of')
    driver.find_element_by_id('txt_F75E3A236075405ABC94001D5E41E3FC_8').send_keys('ever recorded')
    driver.find_element_by_id('txt_F75E3A236075405ABC94001D5E41E3FC_9').send_keys('destructive')
    driver.find_element_by_id('txt_F75E3A236075405ABC94001D5E41E3FC_10').send_keys('injured')

    time.sleep(4)

    driver.find_element_by_css_selector('#btnBottomSubmit').click()
    time.sleep(4)

    driver.switch_to_alert().accept()
    driver.refresh()
    return driver