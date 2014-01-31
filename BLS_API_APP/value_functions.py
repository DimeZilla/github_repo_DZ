# 1. Create conditionals for setting api variables.
from series_id_dict import state_fips, month_series

def get_adjustment():
	
	choose_seasonaladjustment = raw_input("Type 's' or 'u' > ")
	if choose_seasonaladjustment[0].lower() == 's':
		seasonal_adj = 'S'
		return seasonal_adj
	elif choose_seasonaladjustment[0].lower() == 'u':
		seasonal_adj = 'U'
		return seasonal_adj
	else:
		print "invalid adjustment input"
		seasonal_adj = get_adjustment()
		return seasonal_adj
	
	
def decide_state():
	state = raw_input("Type the whole state > ")
	if state in state_fips:
		return state
	else:
		print "invalid state" 
		state = decide_state()
		return state

def get_state(state):
	state_code = state_fips[state]
	return state_code
	


#In the future, we will build out the program to allow for county level choice		
def get_countyFIPS():
	#when we input county choices we will make this a conditional
	pass

	

def get_measurecode():
	#when we learn more about the last parts we will make this a conditional
	choose_measurecode = raw_input("Type the data type > ")
	if choose_measurecode.lower() == "labor force":
		measure_code = "0000000006"
		return measure_code
	elif choose_measurecode.lower() == "employment":
		measure_code = "0000000005"
		return measure_code
	elif choose_measurecode.lower() == "unemployment":
		measure_code = "0000000004"
		return measure_code
	elif choose_measurecode.lower() == "unemployment rate":
		measure_code = "0000000003"
		return measure_code
	else:
		print "Invalid data input"
		measure_code = get_measurecode()
		return measure_code	



def choose_startyear():
	import datetime
	thisyear = datetime.datetime.today().year
	choose_start = raw_input("Choose a startyear > ")
	if len(choose_start) != 4:
		print "invaid year"
		start_year = choose_startyear()
		return start_year
	elif (thisyear - int(choose_start)) > 10: 
		print "The BLS API only allows for from the last ten years."
		print "Please choose a year within the last ten years"
		start_year = choose_startyear()
		return start_year
	else:	
		start_year = choose_start
		return start_year

def choose_endyear():
	import datetime
	thisyear = datetime.datetime.today().year
	choose_end = raw_input("Choose a end year > ")
	if len(choose_end) != 4:
		print "invaid year"
		end_year = choose_endyear()
		return end_year
	elif (thisyear - int(choose_end)) > 10: 
		print "The BLS API only allows for up to ten years worth of data."
		print "Please choose a year within the last ten years"
		end_year = choose_endyear()
		return end_year
	else:	
		end_year = choose_end
		return end_year


