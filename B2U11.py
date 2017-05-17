import time
def b2u11(driver):
    driver.find_element_by_css_selector( '#ctl00_ContentPlaceHolder1_CourseTestTask1_dgTestTask_ctl04_Action > span:nth-child(1) > input:nth-child(1)').click()
    time.sleep(5)
    # 1-5
    driver.find_element_by_id('rd06965AA7138C429CACC50901CAA83300_1_1').click()
    driver.find_element_by_id('rd3C04C93868BE45D8BB762E1FE9ADC533_1_3').click()
    driver.find_element_by_id('rdEEC8B9DE32774B32AEBE69181AA33858_1_4').click()
    driver.find_element_by_id('rdECDDDA478060406B90568B3C2778825F_1_2').click()
    driver.find_element_by_id('rd358CE4642C5D4445AD3835864489E472_1_3').click()
    # #6-10
    driver.find_element_by_id('rd77EB56BA6D954D899B7E10B5BEC2AE1A_1_3').click()
    driver.find_element_by_id('rd77EB56BA6D954D899B7E10B5BEC2AE1A_2_3').click()
    driver.find_element_by_id('rd77EB56BA6D954D899B7E10B5BEC2AE1A_3_3').click()
    driver.find_element_by_id('rd77EB56BA6D954D899B7E10B5BEC2AE1A_4_3').click()
    driver.find_element_by_id('rd77EB56BA6D954D899B7E10B5BEC2AE1A_5_1').click()

    # #11 -15
    driver.find_element_by_id('rdE3FE83F347F54071AA1D0E32429A189D_1_1').click()
    driver.find_element_by_id('rdE3FE83F347F54071AA1D0E32429A189D_2_2').click()
    driver.find_element_by_id('rdE3FE83F347F54071AA1D0E32429A189D_3_1').click()
    driver.find_element_by_id('rdE3FE83F347F54071AA1D0E32429A189D_4_2').click()
    driver.find_element_by_id('rdE3FE83F347F54071AA1D0E32429A189D_5_2').click()
    # 15-20

    driver.find_element_by_id('txt_06F75392976048BAB91A03DC49187332_1').send_keys('dark-haired')
    driver.find_element_by_id('txt_06F75392976048BAB91A03DC49187332_2').send_keys('back entrances')
    driver.find_element_by_id('txt_06F75392976048BAB91A03DC49187332_3').send_keys('thin and hungry')
    driver.find_element_by_id('txt_06F75392976048BAB91A03DC49187332_4').send_keys('drinking')
    driver.find_element_by_id('txt_06F75392976048BAB91A03DC49187332_5').send_keys('hospital')
    driver.find_element_by_id('txt_06F75392976048BAB91A03DC49187332_6').send_keys('impressive accomplishment')
    driver.find_element_by_id('txt_06F75392976048BAB91A03DC49187332_7').send_keys('what he says')
    driver.find_element_by_id('txt_06F75392976048BAB91A03DC49187332_8').send_keys('little actions')
    driver.find_element_by_id('txt_06F75392976048BAB91A03DC49187332_9').send_keys('all over the world')
    driver.find_element_by_id('txt_06F75392976048BAB91A03DC49187332_10').send_keys('his contribution to')

    time.sleep(4)

    driver.find_element_by_css_selector('#btnBottomSubmit').click()
    time.sleep(4)

    driver.switch_to_alert().accept()
    driver.refresh()
    return driver