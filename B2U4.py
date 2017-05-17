import time

def b2u4(driver):
    #driver.find_element_by_css_selector('#ctl00_ContentPlaceHolder1_CourseTestTask1_dgTestTask_ctl19_PAGER > div > ul > li.enablepage > a').click()
    driver.find_element_by_css_selector('#ctl00_ContentPlaceHolder1_CourseTestTask1_dgTestTask_ctl14_Action > span > input[type="button"]').click()
    time.sleep(5)
    # 1-5
    driver.find_element_by_id('rd689C33977C3944F3B94F091ABA4BBA76_1_3').click()
    driver.find_element_by_id('rd44521329E5B141999B77961AD5B9C70D_1_4').click()
    driver.find_element_by_id('rdB6B00CDBD0D84ADE8D60A4C6513FE65C_1_3').click()
    driver.find_element_by_id('rd9E6C77526147463A89089414A6D65274_1_2').click()
    driver.find_element_by_id('rd25799457BE944E908D09C0EDE3DC5E22_1_2').click()

    # #6-15
    driver.find_element_by_id('txt_086F10348614495D8682AF27B03ACF0A_1').send_keys('received')
    driver.find_element_by_id('txt_086F10348614495D8682AF27B03ACF0A_2').send_keys('best new artist')
    driver.find_element_by_id('txt_086F10348614495D8682AF27B03ACF0A_3').send_keys('announce')
    driver.find_element_by_id('txt_086F10348614495D8682AF27B03ACF0A_4').send_keys('Hip-hop')
    driver.find_element_by_id('txt_086F10348614495D8682AF27B03ACF0A_5').send_keys('song of the year')
    driver.find_element_by_id('txt_086F10348614495D8682AF27B03ACF0A_6').send_keys('eleven')
    driver.find_element_by_id('txt_086F10348614495D8682AF27B03ACF0A_7').send_keys('album of the year award')
    driver.find_element_by_id('txt_086F10348614495D8682AF27B03ACF0A_8').send_keys('release')
    driver.find_element_by_id('txt_086F10348614495D8682AF27B03ACF0A_9').send_keys('alternative')
    driver.find_element_by_id('txt_086F10348614495D8682AF27B03ACF0A_10').send_keys('two-man band')

    driver.find_element_by_id('rd5EA04AD1E107482D922BF19AB7F076F1_1_1').click()
    driver.find_element_by_id('rd5EA04AD1E107482D922BF19AB7F076F1_2_2').click()
    driver.find_element_by_id('rd5EA04AD1E107482D922BF19AB7F076F1_3_1').click()
    driver.find_element_by_id('rd5EA04AD1E107482D922BF19AB7F076F1_4_1').click()
    driver.find_element_by_id('rd5EA04AD1E107482D922BF19AB7F076F1_5_2').click()
    # 16 -25

    driver.find_element_by_id('txt_0C4532D92B9D424EBB4557E792F3D676_1').send_keys('August 29th, 1920')
    driver.find_element_by_id('txt_0C4532D92B9D424EBB4557E792F3D676_2').send_keys('western state')
    driver.find_element_by_id('txt_0C4532D92B9D424EBB4557E792F3D676_3').send_keys('1932')
    driver.find_element_by_id('txt_0C4532D92B9D424EBB4557E792F3D676_4').send_keys('mother')
    driver.find_element_by_id('txt_0C4532D92B9D424EBB4557E792F3D676_5').send_keys('1934')
    driver.find_element_by_id('txt_0C4532D92B9D424EBB4557E792F3D676_6').send_keys('leave school')
    driver.find_element_by_id('txt_0C4532D92B9D424EBB4557E792F3D676_7').send_keys('professional')
    driver.find_element_by_id('txt_0C4532D92B9D424EBB4557E792F3D676_8').send_keys('popular')
    driver.find_element_by_id('txt_0C4532D92B9D424EBB4557E792F3D676_9').send_keys('playing with different groups')
    driver.find_element_by_id('txt_0C4532D92B9D424EBB4557E792F3D676_10').send_keys('listening to older local jazz musicians')

    time.sleep(4)

    driver.find_element_by_css_selector('#btnBottomSubmit').click()
    time.sleep(4)

    driver.switch_to_alert().accept()
    driver.refresh()
    return driver
