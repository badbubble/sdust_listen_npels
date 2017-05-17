import time
def b2u3(driver):
    driver.find_element_by_css_selector( '#ctl00_ContentPlaceHolder1_CourseTestTask1_dgTestTask_ctl15_Action > span > input[type="button"]').click()
    time.sleep(5)
    # 1-5
    driver.find_element_by_id('rd33910725DC164E1BA5EF4856703007DA_1_3').click()
    driver.find_element_by_id('rdFEA0B86AA64F463DBB28250426A42D38_1_2').click()
    driver.find_element_by_id('rdD4034AB0EFA7498AB1B826BD53DF8DD2_1_1').click()
    driver.find_element_by_id('rd9209F58345ED49E884C10FF60C5F4771_1_1').click()
    driver.find_element_by_id('rd7176BC956C6C4DE5ACBEE119A1D61B1D_1_3').click()
    # #6-15
    driver.find_element_by_id('txt_08D4F901F610443CA5D750E27179A385_1').send_keys('precise instruments')
    driver.find_element_by_id('txt_08D4F901F610443CA5D750E27179A385_2').send_keys('passed down')
    driver.find_element_by_id('txt_08D4F901F610443CA5D750E27179A385_3').send_keys('in the form of')
    driver.find_element_by_id('txt_08D4F901F610443CA5D750E27179A385_4').send_keys('reliable')
    driver.find_element_by_id('txt_08D4F901F610443CA5D750E27179A385_5').send_keys('stop')
    driver.find_element_by_id('txt_08D4F901F610443CA5D750E27179A385_6').send_keys('sailor\'s delight')
    driver.find_element_by_id('txt_08D4F901F610443CA5D750E27179A385_7').send_keys('storm')
    driver.find_element_by_id('txt_08D4F901F610443CA5D750E27179A385_8').send_keys('autumn')
    driver.find_element_by_id('txt_08D4F901F610443CA5D750E27179A385_9').send_keys('mouth')
    driver.find_element_by_id('txt_08D4F901F610443CA5D750E27179A385_10').send_keys('pillar')

    # #16 -20
    driver.find_element_by_id('rdE8F4E1AE345E42D5B4CB569BC8DDF6E0_1_2').click()
    driver.find_element_by_id('rdE8F4E1AE345E42D5B4CB569BC8DDF6E0_2_1').click()
    driver.find_element_by_id('rdE8F4E1AE345E42D5B4CB569BC8DDF6E0_3_1').click()
    driver.find_element_by_id('rdE8F4E1AE345E42D5B4CB569BC8DDF6E0_4_2').click()
    driver.find_element_by_id('rdE8F4E1AE345E42D5B4CB569BC8DDF6E0_5_1').click()
    # 21 -30

    driver.find_element_by_id('txt_8A836234A38948F4BF97ECF1B5C556A7_1').send_keys('Flooding')
    driver.find_element_by_id('txt_8A836234A38948F4BF97ECF1B5C556A7_2').send_keys('Above-average rainfall')
    driver.find_element_by_id('txt_8A836234A38948F4BF97ECF1B5C556A7_3').send_keys('Above-average rainfall')
    driver.find_element_by_id('txt_8A836234A38948F4BF97ECF1B5C556A7_4').send_keys('Texas')
    driver.find_element_by_id('txt_8A836234A38948F4BF97ECF1B5C556A7_5').send_keys('Drought')
    driver.find_element_by_id('txt_8A836234A38948F4BF97ECF1B5C556A7_6').send_keys('hurricane')
    driver.find_element_by_id('txt_8A836234A38948F4BF97ECF1B5C556A7_7').send_keys('get any worse than this')
    driver.find_element_by_id('txt_8A836234A38948F4BF97ECF1B5C556A7_8').send_keys('compared to')
    driver.find_element_by_id('txt_8A836234A38948F4BF97ECF1B5C556A7_9').send_keys('In fact')
    driver.find_element_by_id('txt_8A836234A38948F4BF97ECF1B5C556A7_10').send_keys('ever recorded')

    time.sleep(4)

    driver.find_element_by_css_selector('#btnBottomSubmit').click()
    time.sleep(4)

    driver.switch_to_alert().accept()
    driver.refresh()
    return driver