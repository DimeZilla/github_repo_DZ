print "Welcome to the unemployment stats program!"
print "Let's get some unemployment data!"

import blsapp as bp 

# Lets get this sucker started!

def launch(): 
	data = bp.start()
	bp.data_output(data)

	print "Would you like to find another state's unemployment data?"

	choose_continue = raw_input("Type yes or no > ")
	if choose_continue[0].lower() == "y":
		print "Alright lets continue."
		launch()
	elif choose_continue[0].lower == "n":
		print "Thank you! Goodbye"
		exit()

launch()