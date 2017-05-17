import time
def b2u1(driver):
    driver.find_element_by_css_selector('#ctl00_ContentPlaceHolder1_CourseTestTask1_dgTestTask_ctl03_Action > span > input[type="button"]').click()
    time.sleep(5)
    # 1-5
    driver.find_element_by_id('rd194D24158B1D4A48AAA7335A2BA3F2E0_1_2').click()
    driver.find_element_by_id('rd5C118817E94B4266B95FD80D8A70C979_1_3').click()
    driver.find_element_by_id('rd936C42298A7D411788C482F6E85ED7F0_1_4').click()
    driver.find_element_by_id('rd18AB5E320F574D3C95DAA0CBF19E7620_1_1').click()
    driver.find_element_by_id('rd041E891310F1453EB2F7ECF7F0344561_1_2').click()
    # #6-10
    driver.find_element_by_id('rdF14574F608964741958DCE1BD9A05056_1_2').click()
    driver.find_element_by_id('rd4B86410F3FB0400998E5DBCEE06961F6_1_2').click()
    driver.find_element_by_id('rd52968B81A82E4FF8B32CAF929F982422_1_4').click()
    driver.find_element_by_id('rd0C55CEB7EF0348B09A046A60C1E3EB14_1_3').click()
    driver.find_element_by_id('rd63AEC40CD58A4E06A05C374CDCB9E348_1_3').click()
    # # #11 -15
    driver.find_element_by_id('rdFCE14FCC79B546779172C6ED059976E4_1_1').click()
    driver.find_element_by_id('rd49AC891EF18449379A59D8DB3032F675_1_2').click()
    driver.find_element_by_id('rdCFA0AB88C594496E93F449D983010A92_1_4').click()
    driver.find_element_by_id('rd9A4641124DB2470FA382295F98F59044_1_2').click()
    driver.find_element_by_id('rd60538085047C4F46A0B46A8E011E6DBC_1_2').click()
    # #16 -20
    driver.find_element_by_id('rd5C0F88423D8C4080B23CC2E1A2845B47_1_2').click()
    driver.find_element_by_id('rd5C0F88423D8C4080B23CC2E1A2845B47_2_1').click()
    driver.find_element_by_id('rd5C0F88423D8C4080B23CC2E1A2845B47_3_1').click()
    driver.find_element_by_id('rd5C0F88423D8C4080B23CC2E1A2845B47_4_2').click()
    driver.find_element_by_id('rd5C0F88423D8C4080B23CC2E1A2845B47_5_1').click()
    # 21 -30

    driver.find_element_by_id('txt_61F9AF93046448CD917B6D46BBC8E6E6_1').send_keys('look up')
    driver.find_element_by_id('txt_61F9AF93046448CD917B6D46BBC8E6E6_2').send_keys('guess')
    driver.find_element_by_id('txt_61F9AF93046448CD917B6D46BBC8E6E6_3').send_keys('figure out')
    driver.find_element_by_id('txt_61F9AF93046448CD917B6D46BBC8E6E6_4').send_keys('biggest')
    driver.find_element_by_id('txt_61F9AF93046448CD917B6D46BBC8E6E6_5').send_keys('keep a vocabulary book')
    driver.find_element_by_id('txt_61F9AF93046448CD917B6D46BBC8E6E6_6').send_keys('translation')
    driver.find_element_by_id('txt_61F9AF93046448CD917B6D46BBC8E6E6_7').send_keys('sentence')
    driver.find_element_by_id('txt_61F9AF93046448CD917B6D46BBC8E6E6_8').send_keys('group together')
    driver.find_element_by_id('txt_61F9AF93046448CD917B6D46BBC8E6E6_9').send_keys('didn\'t work')
    driver.find_element_by_id('txt_61F9AF93046448CD917B6D46BBC8E6E6_10').send_keys('use them')

    time.sleep(4)

    driver.find_element_by_css_selector('#btnBottomSubmit').click()
    time.sleep(4)

    driver.switch_to_alert().accept()
    driver.refresh()
    return driver
