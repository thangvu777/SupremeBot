###################################################################
# Currently as of 07/08/2019
# Supreme allows for 2019 - 2029 as card expiration years
# In XPATH, that's 1 - 11 in the xpath selector for that drop down.
# [1:2019, 2:2020, ..., 11: 2029]
# Author: Thang Vu
###################################################################

# This dictionary contains all the information you will fill in
# my computer finishes filling this in at less than 3 seconds
# this will help you secure the item you want

# modify the information below to your information

# beware: state, card expiration month, and card expiration year
# needs to be formatted correctly.

# beware 2: all orders need to be filled with a different credit card
# The Supreme website only allows one order to one credit card. 

keys = {
	# unique product url... must replace at every drop
	"product_url" : "https://www.supremenewyork.com/shop/shirts/v5wunv0js",
	"name" : "John Doe",
	"email" : "John_Doe@gmail.com",
	"phone_number": "123-456-7890",
	"address" : "4812 Kelly Drive", #format is "###-###-###"
	"address2" : "", # apt, suit, etc
	"zip" : "75013", 
	"city" : "Allen", 
	"state" : "TX", # format is "TX" = TX, "AZ" = AZ, "NY" = NY,... Type "ZZ". ZZ = State abbreviation
	"card_number" : "4266841612190161", #format is "################" that is 16 digits...
	"card_cvv" : "960", # format is "###"
	"card_exp_mo": "11", # format is "#" (1 - 12)
	"card_exp_yr" : "5", # format is "#" (1 - 10). 5 = 2023... See documentation above for more information
}
