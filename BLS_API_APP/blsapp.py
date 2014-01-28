# This is a side project
		## Defining API Call ##
#OBJECTIVE: Defining whether or not to get unemployment data by state or by county
# All unemployment data will be non-seasonally adjusted

#	1. Create conditionals for selecting api variables
		# A. State
			# Which state
		# B. County
			# Which state


		## Connecting to the BLS data and retrieving results ##
#OBJCTIVE: Connect to the API based off of the user selections and retrieve data.


		# Visualizing Results
#OBJECTIVE: display the api results in a user-friendly way with options for
#exporting to csv, mapping, charting
#	4. Format Results in a user formatted way
		# - allow for export to csv
#	5. Map results by county or national results
# 	6. Chart results along a time seriese
#	7. scatter plot averages by month regardless of year
#	8. histogram of average for that month regardless of year
#	9. Labor Force / Total Pop

# MAKE THIS DATA ALL FREE ON YOUR WEBSITE
	# MAKE MONEY ADVERTISING - GOTTA LIVE AFTER GETTING FIRED FROM JOB
# HAVE A FUN TIME LEARNING PYTHON!
 

#get geo dictionary
from series_id_dict import state_fips
from api import get_data
import datetime
# 1. Create conditionals for setting api variables.

print "Let's Get unemployment data from teh last three years."

def get_seriesid():

	

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
			get_adjustment()
	
	

	
	def get_state():
		choose_state = raw_input("Type a state name > ")
		if choose_state in state_fips:
			state_code = state_fips[choose_state]
			return state_code
		else:
			print "invalid state" 
			get_state()


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
			get_measurecode()
	
	level = "ST"
	print "Do you want your data to be seasonally adjusted or unseasonally adjusted?"
	print "Warning: county level data is only available as unseasonally adjusted."	
	seasonal_adj = get_adjustment()
	print "Choose which state you want to Get Data for."
	state_code = get_state()
	print "Choose which type of data you want."
	print """
			Labor Force
			Employment
			Unemployment
			Unemployment Rate
			"""
	measure_code = get_measurecode()

	# the "000" will have to be modified when we add county level choices
	series_id = "LA" + seasonal_adj + level + state_code + "000" + measure_code	
	return series_id		


thisyear = datetime.datetime.today().year

def choose_startyear():
	choose_start = raw_input("Choose a startyear > ")
	if len(choose_start) != 4:
		print "invaid year"
		startyear()
	elif (thisyear - int(choose_start)) > 10: 
		print "The BLS API only allows for from the last ten years."
		print "Please choose a year within the last ten years"
		startyear()
	else:	
		start_year = choose_start
		return start_year



def choose_endyear():
	choose_end = raw_input("Choose a end year > ")
	if len(choose_end) != 4:
		print "invaid year"
		choose_endyear()
	elif (thisyear - int(choose_end)) > 10: 
		print "The BLS API only allows for up to ten years worth of data."
		print "Please choose a year within the last ten years"
		choose_endyear()
	else:	
		end_year = choose_end
		return end_year


# Lets Party like we're an unemployment stat!
series_id = get_seriesid()
start_year = choose_startyear()
end_year = choose_endyear()

#Get API call and retrieve data
from api import get_data
apidata = get_data(series_id,start_year,end_year)
print apidata
