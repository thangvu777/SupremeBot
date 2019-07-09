# Author: Thang Vu

# OBJECTIVE: This is a bot designed to automatically launch chrome and purchase low stock items
# on Supreme New York. This program helps its users get their hands on items that sell out within
# seconds because these items are in high-demand and have high resell value. This project
# can help it's users create revenue by reselling the items that they buy for retail price.
# Items from Supreme website can be resold for ()

# TOOLS: This project utilizes the google webdriver as well as xpath directories to find anchors 
# for webscraping 


# To open Chrome we must have webdriver
from selenium import webdriver
# Dictionary with user's information... (Must be customized for every unique order)
from config import keys
# Sleep function for page buffers
import time

# this function times other methods
def timefunction(method):
    def function_container(*args, **kw):
        startTime = int(round(time.time() * 10000))
        result = method(*args, **kw)
        endTime = int(round(time.time() * 10000))
        print((endTime - startTime)/10000, 's')
        return result
    return function_container

#time order function
@timefunction
#pass in dictionary
def order(k, k2):
	#Get url from key
	driver.get(k['product_url'])
	#find anchors
	# inspect by x path and get button anchors and click
	driver.find_element_by_xpath('//*[@id="add-remove-buttons"]/input').click()
	# add buffer to stall for button to appear
	time.sleep(.4)
	driver.find_element_by_xpath('//*[@id="cart"]/a[2]').click()
	#fill in the keys
	# name, must be first and last name
	driver.find_element_by_xpath('//*[@id="order_billing_name"]').send_keys(k["name"])
	# email
	driver.find_element_by_xpath('//*[@id="order_email"]').send_keys(k["email"])
	# phone number format is "###-###-####"
	driver.find_element_by_xpath('//*[@id="order_tel"]').send_keys(k["phone_number"])
	# shipping address (must be same as billing address)
	driver.find_element_by_xpath('//*[@id="bo"]').send_keys(k["address"])

	# ADDRESS 2 (APT, SUITE, ETC...) MUST DELETE "#" to activate code
	# driver.find_element_by_xpath('//*[@id="oba3"]').send_keys(k["address2"])

	# zip code
	driver.find_element_by_xpath('//*[@id="order_billing_zip"]').send_keys(k["zip"])
	# city
	driver.find_element_by_xpath('//*[@id="order_billing_city"]').send_keys(k["city"])

	# state... automatically parsed
	state_number = getStateNumber(k["state"], k2)
	driver.find_element_by_xpath('//*[@id="order_billing_state"]/option[{}]'.format(state_number)).click()

	# card number
	driver.find_element_by_xpath('//*[@id="nnaerb"]').send_keys(k["card_number"])
	# cvv code
	driver.find_element_by_xpath('//*[@id="orcer"]').send_keys(k["card_cvv"])
	# expiration month
	driver.find_element_by_xpath('//*[@id="credit_card_month"]/option[{}]'.format(k["card_exp_mo"])).click()
	#option 1 = 2019, option 2 = 2020, ... , option 11 = 2029
	driver.find_element_by_xpath('//*[@id="credit_card_year"]/option[{}]'.format(k["card_exp_yr"])).click()
	
	# terms and conditions agreement
	driver.find_element_by_xpath('//*[@id="cart-cc"]/fieldset/p[2]/label/div/ins').click() 
	# confirm payment
	driver.find_element_by_xpath('//*[@id="pay"]/input').click() 
	# you should be sent to capta at this point.


# function that returns the state number in Xcode
def getStateNumber(stateAbbreviation, keys):
	return keys.get(stateAbbreviation)

# DONOT TOUCH STATES_KEYS unless another state gets annexed to the US...
states_keys = {
	"AL" : 1, "AK" : 2, "AS" : 3, "AZ" : 4, "AR" : 5, "CA" : 6, "CO" : 7, "CT" : 8, "DE" : 9, "DC" : 10, "FM" : 11, "FL" : 12,
	"GA" : 13, "GU" : 14, "HI" : 15, "ID" : 16, "IL" : 17, "IN" : 18, "IA" : 19, "KS" : 20, "KY" : 21, "LA" : 22, "ME" : 23, 
	"MH" : 24, "MD" : 25, "MA" : 26, "MI" : 27, "MN" : 28, "MS" : 29, "MO" : 30, "MT" : 31, "NE" : 32, "NV" : 33, "NH" : 34, 
	"NJ" : 35, "NM" : 36, "NY" : 37, "NC" : 38, "ND" : 39, "MP" : 40, "OH" : 41, "OK" : 42, "OR" : 43, "PW" : 44, "PA" : 45,
	"PR" : 46, "RI" : 47, "SC" : 48, "SD" : 49, "TN" : 50, "TX" : 51, "UT" : 52, "VT" : 53, "VI" : 54, "VA" : 55, "WA" : 56, 
	"WV" : 57, "WI" : 58, "WY" : 59
}

if __name__ == '__main__':
	#"Chrome is being controlled by automated test software." error
	# Must disable infobars by adjusting the options in the driver
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument("--disable-infobars")
	#Open chrome
	driver = webdriver.Chrome('./chromedriver')
	#Call order function
	order(keys, states_keys)
