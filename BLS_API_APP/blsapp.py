

from api import get_data
import value_functions as vf


# Lets Party like we're an unemployment stat!

def start()	:
	#choose state
	print "Choose which state you want to Get Data for."
	state = vf.decide_state()
	state_code = str(vf.get_state(state))
	
	level = "ST"
		
	#Get adjustment value
	print "Do you want your data to be seasonally adjusted or unseasonally adjusted?"
	print "Warning: county level data is only available as unseasonally adjusted."
	seasonal_adj = vf.get_adjustment()

	print "Choose which type of data you want."
	print """
	Labor Force
	Employment
	Unemployment
	Unemployment Rate
	"""
	measure_code = str(vf.get_measurecode())
	
	series_id = "LA" + seasonal_adj + level + state_code + "000" + measure_code
	
	#set start and end years
	start_year = vf.choose_startyear()
	end_year = vf.choose_endyear()


	# the "000" will have to be modified when we add county level choices
	#Get API call and retrieve data
	from api import get_data
	apidata = get_data(series_id,start_year,end_year, state)
	return apidata



def data_output(data):
		print "Good News! You're data has been returned. I'm happy to show it to you."
		print "Just tell me how you want it - Table or Line Graph?"

		data_output = raw_input("Choose table or line > ")

		if data_output[0].lower() == "t":
			print "Ok, here's your data."
			print data
		elif data_output[0] == "l" or data_output[0].lower() =="g":
			from ggplot import *

			plot = ggplot(aes(x='Order', y='Value'), data=data) + \
    			geom_point(color='black') + \
    			geom_line(color='green') + \
    			ggtitle("Unemployment Data") + \
    			xlab("Month, Year") + \
    			ylab("Value") 
    			# scale_x_date(breaks = date_breaks('1 month'), labels=date_format("%B")) + \ - working on adding dates to xaxis
			print (plot + theme_xkcd())
			plt.show(1)

