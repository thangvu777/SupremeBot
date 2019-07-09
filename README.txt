Author: Thang Vu
INSTRUCTIONS FOR SUPREME BOT
#Get sublime text, vim, or use your current text editor to modify config.py to 
#modify your order information

#Follow all the steps below to run the bot
#Skip steps if you have already have the item installed...

SET UP:

1: Install latest version of PYTHON on your computer
	-Add to PATH environment variable on your PC so you can use python in cmd
2: Download get-pip.py. Locate the file in cmd and install by using command "python get-pip.py"
	-Check if pip was installed correctly by using command "pip -V"
3: Install selenium by using command "pip install selenium"
4: Install Google Chrome.
5: Create a folder on your Desktop and download "config.py", and "bot.py" into the folder
6: Download Chrome Driver. Check which version of Google Chrome you are using
	-Click the 3 dots near the top right of the browser "customize and control Google Chrome"
	-Hover over "Help"
	-Click "About Google Chrome," and check the version
7: Download the Google Chrome Driver .zip file for your version of Google Chrome in the folder you created in step [5] your Desktop.
	-visit https://sites.google.com/a/chromium.org/chromedriver/downloads
	-Unzip/export the google driver into the folder that you created in step [5] on your Desktop.


# Once set up is complete, this step can be repeated many times to make additional orders

EXECUTION:

8: Modify your order in config.py using a text editor (I personally prefer sublime text, it's intuitive and free)
	-This includes the
		-product URL, this is unique for all products so make sure you specify the specific item you want to purchase
		-your name (first and last)
		-email
		-phone number in the format "###-###-###"
		-address
		-address2: this is for apt, suite, etc
			- If you do have live in an apartment or suite, you have to delete the "#" in front of the code in line 47 of 
			- bot.py
		-city
		-state
		-credit card number
		-card's security cvv number
		-card expiration month format (1-12)
		-card expiration year (1-11) 1 is your current year... At the time this was written it was 2019. so 1-11 covered 2019 - 2029

9: Run bot.py in cmd using ("python bot.py") during the drop
10: The bot will finish filling in your information in roughly ~2.5 seconds, report to you the execution time,
    and allow you to MANUALLY enter in the capta and click verify.
11: Chrome will then take you to the confirmation and shipping page.
12: GOOD LUCK
