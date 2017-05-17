import time

def b2u13(driver):
    driver.find_element_by_css_selector( '#ctl00_ContentPlaceHolder1_CourseTestTask1_dgTestTask_ctl12_Action > span > input[type="button"]').click()
    time.sleep(5)
    # 1-5

    driver.find_element_by_id('rd21DDFA06DEDD4BA6B071289B5A6F3FB8_1_3').click()
    driver.find_element_by_id('rd49BCFEE583E34CC2907CA97FBBE8C7BE_1_2').click()
    driver.find_element_by_id('rd51BE4171101342C69E03D93316848A19_1_1').click()
    driver.find_element_by_id('rd9FF417D9320D4B419703B0C68EB6BB1B_1_1').click()
    driver.find_element_by_id('rdCD946AA06CA14E07B30E7ADE6D09C509_1_4').click()
    # #6-15
    driver.find_element_by_id('txt_65734723496C4038B5F390B307B9A3E0_1').send_keys('forgiveness')
    driver.find_element_by_id('txt_65734723496C4038B5F390B307B9A3E0_2').send_keys('shortcomings')
    driver.find_element_by_id('txt_65734723496C4038B5F390B307B9A3E0_3').send_keys('fall short of')
    driver.find_element_by_id('txt_65734723496C4038B5F390B307B9A3E0_4').send_keys('reflect')
    driver.find_element_by_id('txt_65734723496C4038B5F390B307B9A3E0_5').send_keys('evaluating')
    driver.find_element_by_id('txt_65734723496C4038B5F390B307B9A3E0_6').send_keys('prevented')
    driver.find_element_by_id('txt_65734723496C4038B5F390B307B9A3E0_7').send_keys('situation')
    driver.find_element_by_id('txt_65734723496C4038B5F390B307B9A3E0_8').send_keys('glory')
    driver.find_element_by_id('txt_65734723496C4038B5F390B307B9A3E0_9').send_keys('pride')
    driver.find_element_by_id('txt_65734723496C4038B5F390B307B9A3E0_10').send_keys('reconciliation and restoration')

    # #16 -20
    driver.find_element_by_id('rd1EFF5658E36E46EE903DC37EA7746D2B_1_1').click()
    driver.find_element_by_id('rd1EFF5658E36E46EE903DC37EA7746D2B_2_2').click()
    driver.find_element_by_id('rd1EFF5658E36E46EE903DC37EA7746D2B_3_1').click()
    driver.find_element_by_id('rd1EFF5658E36E46EE903DC37EA7746D2B_4_2').click()
    driver.find_element_by_id('rd1EFF5658E36E46EE903DC37EA7746D2B_5_1').click()
    # 21 -30

    driver.find_element_by_id('txt_5D45F30C96CD4A78934C87BFA2E76805_1').send_keys('perseverance')
    driver.find_element_by_id('txt_5D45F30C96CD4A78934C87BFA2E76805_2').send_keys('management training program')
    driver.find_element_by_id('txt_5D45F30C96CD4A78934C87BFA2E76805_3').send_keys('first job')
    driver.find_element_by_id('txt_5D45F30C96CD4A78934C87BFA2E76805_4').send_keys('work your way to the top')
    driver.find_element_by_id('txt_5D45F30C96CD4A78934C87BFA2E76805_5').send_keys('ended up')
    driver.find_element_by_id('txt_5D45F30C96CD4A78934C87BFA2E76805_6').send_keys('terrific run')
    driver.find_element_by_id('txt_5D45F30C96CD4A78934C87BFA2E76805_7').send_keys('devoted')
    driver.find_element_by_id('txt_5D45F30C96CD4A78934C87BFA2E76805_8').send_keys('impressively')
    driver.find_element_by_id('txt_5D45F30C96CD4A78934C87BFA2E76805_9').send_keys('considered')
    driver.find_element_by_id('txt_5D45F30C96CD4A78934C87BFA2E76805_10').send_keys('passed over')

    time.sleep(4)

    driver.find_element_by_css_selector('#btnBottomSubmit').click()
    time.sleep(4)

    driver.switch_to_alert().accept()
    driver.refresh()
    return driver