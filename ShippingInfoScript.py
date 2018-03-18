__author__ = 'machongshen'

from selenium import webdriver

ls = ["10000522716",
"10000522714",
"10000522711",
"10000522712",
"10000522713",
"10000522720",
"10000522721",
"10000562603",
"10000562604",
"10000562624",
"10000562626",
"10000562627", ]
res = []
for order in ls:
    options = webdriver.ChromeOptions()
    options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    chrome_driver_binary = "/usr/local/bin/chromedriver/"
    driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
    driver.get('http://worldcps.com/index.html')

    # type text
    text_area = driver.find_elements_by_xpath("//input")[0]
    text_area.send_keys(order)

    submit_button = driver.find_elements_by_xpath('//*[@class="search_btn  fr "]')[0]
    submit_button.click()

    elem = driver.find_element_by_xpath("//ul[@class='trans_info  clearfix tl ml20 ']")
    res.append(" ".join(elem.text.split("\n")[:2]))
    s = " ".join(elem.text.split("\n")[:2])
    print(f'order no: {order}   status: {s}')
    driver.close()
