import time

def b2u8(driver):
    #driver.find_element_by_css_selector('#ctl00_ContentPlaceHolder1_CourseTestTask1_dgTestTask_ctl19_PAGER > div > ul > li.enablepage > a').click()
    driver.find_element_by_css_selector('#ctl00_ContentPlaceHolder1_CourseTestTask1_dgTestTask_ctl07_Action > span > input[type="button"]').click()
    time.sleep(5)
    # 1-5
    driver.find_element_by_id('rd10ECAAAEADF34952A2F96F27A7D11967_1_3').click()
    driver.find_element_by_id('rd9D809B3B14F7499BB0EDBA7B361F78B0_1_3').click()
    driver.find_element_by_id('rd74EA431B814145A39023E032E2CC561E_1_2').click()
    driver.find_element_by_id('rd86C0CA2F286845C69D5EBD5783327DF4_1_4').click()
    driver.find_element_by_id('rd0D0509D5376042E189D8488461272A5B_1_3').click()

    # #6-15
    driver.find_element_by_id('txt_996BF51DB0284F57B04EB6DDB06AD004_1').send_keys('1999')
    driver.find_element_by_id('txt_996BF51DB0284F57B04EB6DDB06AD004_2').send_keys('july 28')
    driver.find_element_by_id('txt_996BF51DB0284F57B04EB6DDB06AD004_3').send_keys('funds')
    driver.find_element_by_id('txt_996BF51DB0284F57B04EB6DDB06AD004_4').send_keys('Civil Affairs')
    driver.find_element_by_id('txt_996BF51DB0284F57B04EB6DDB06AD004_5').send_keys('1997')
    driver.find_element_by_id('txt_996BF51DB0284F57B04EB6DDB06AD004_6').send_keys('1.41 billion')
    driver.find_element_by_id('txt_996BF51DB0284F57B04EB6DDB06AD004_7').send_keys(' 81,000')
    driver.find_element_by_id('txt_996BF51DB0284F57B04EB6DDB06AD004_8').send_keys('pushed forward')
    driver.find_element_by_id('txt_996BF51DB0284F57B04EB6DDB06AD004_9').send_keys(' 74,750')
    driver.find_element_by_id('txt_996BF51DB0284F57B04EB6DDB06AD004_10').send_keys('windfalls')

    driver.find_element_by_id('rdC8A831AED8A04760BA53842A7531FB0B_1_1').click()
    driver.find_element_by_id('rdC8A831AED8A04760BA53842A7531FB0B_2_1').click()
    driver.find_element_by_id('rdC8A831AED8A04760BA53842A7531FB0B_3_1').click()
    driver.find_element_by_id('rdC8A831AED8A04760BA53842A7531FB0B_4_2').click()
    driver.find_element_by_id('rdC8A831AED8A04760BA53842A7531FB0B_5_1').click()
    # 16 -25

    driver.find_element_by_id('txt_35C6A00D5FC74F2991BF0A6D8DC32412_1').send_keys('instant riches')
    driver.find_element_by_id('txt_35C6A00D5FC74F2991BF0A6D8DC32412_2').send_keys('at random')
    driver.find_element_by_id('txt_35C6A00D5FC74F2991BF0A6D8DC32412_3').send_keys('hope for')
    driver.find_element_by_id('txt_35C6A00D5FC74F2991BF0A6D8DC32412_4').send_keys('turNing into')
    driver.find_element_by_id('txt_35C6A00D5FC74F2991BF0A6D8DC32412_5').send_keys('astronomical')
    driver.find_element_by_id('txt_35C6A00D5FC74F2991BF0A6D8DC32412_6').send_keys('miraculous')
    driver.find_element_by_id('txt_35C6A00D5FC74F2991BF0A6D8DC32412_7').send_keys('claimed')
    driver.find_element_by_id('txt_35C6A00D5FC74F2991BF0A6D8DC32412_8').send_keys('bank account')
    driver.find_element_by_id('txt_35C6A00D5FC74F2991BF0A6D8DC32412_9').send_keys('entertainment purposes')
    driver.find_element_by_id('txt_35C6A00D5FC74F2991BF0A6D8DC32412_10').send_keys('heartache')

    time.sleep(4)

    driver.find_element_by_css_selector('#btnBottomSubmit').click()
    time.sleep(4)

    driver.switch_to_alert().accept()
    driver.refresh()
    return driver