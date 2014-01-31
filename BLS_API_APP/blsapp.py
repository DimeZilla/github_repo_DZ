from output import data_output
import value_functions as vf
from series_id_dict import state_fips
from api import get_data
# Lets get this sucker started!

print "Welcome to the unemployment stats program!"
print "Let's get some unemployment data!"

def start(): 

	print "Choose which state you want to Get Data for."
	state = vf.decide_state()
	state_code = str(state_fips[state]) #get state_code
	print "Do you want your data to be seasonally adjusted or unseasonally adjusted?"
	print "Warning: county level data is only available as unseasonally adjusted."
	seasonal_adj = vf.get_adjustment()
	level = "ST"
	print "Choose which type of data you want."
	print """
	Labor Force
	Employment
	Unemployment
	Unemployment Rate
	"""
	measure_code = str(vf.get_measurecode())
	series_id = "LA" + seasonal_adj + level + state_code + "000" + measure_code
	start_year = vf.choose_startyear()
	end_year = vf.choose_endyear()

	apidata=get_data(series_id, start_year, end_year, state)
	chart_title = vf.get_charttitle(state,measure_code, start_year, end_year)
	data_output(apidata, chart_title) #start graphing and tabling!

	print "Would you like to find another state's unemployment data?"

	choose_continue = raw_input("Type yes or no > ")
	if choose_continue[0].lower() == "y":
		print "Alright lets continue."
		start()
	elif choose_continue[0].lower == "n":
		print "Thank you! Goodbye"
		exit()

start()