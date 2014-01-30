#	Connect to BLS API
#	Retrieve monthly unemployment rates and raw numbers going back 10 years by
		# A. State
		# B. county
	#	Return results 

from ggplot import *
from pandas import *

# series_id = 'LASST010000000000003'
# start_year = '2013'
# end_year = '2013'
# state = 'Alabama'
	
def get_data(series_id, start_year, end_year, state):
	from urllib2 import Request, urlopen
	from urllib import urlencode
	import json
	

	# BLS api url
	url = 'http://api.bls.gov/publicAPI/v1/timeseries/data/'
	# Set header to pass to bls api
	headers = {"Content-Type": "application/json"}

	values = {
		"seriesid":[series_id],
		"startyear": str(start_year),
		"endyear": str(end_year)
		}


	# Encode the values, connect to api, decode response data retrieve data
	data = json.dumps(values).encode()
	req = Request(url,data,headers)
	response = urlopen(req).read()
	decoded_response = json.loads(response.decode())
	results = decoded_response["Results"]
	
	def format_results(results, state):
		dump = results["series"][0]["data"]
		# ptest = dump[0]["footnotes"][0]["code"] - will eventually use to exclue preliminary data
		
		#format returned data into a dictionary
		formatted = {'Order':list(), 'State': list(), 'Value': list(), 'Month, Year': list()}
		for i in range(len(dump)-1,-1,-1):
			formatted['State'].append(state)
			formatted['Value'].append(dump[i]["value"])
			formatted['Month, Year'].append(dump[i]["periodName"]+", "+dump[i]["year"])
		
		#set ordinal column for plotting
		for i in range(len(dump)):
			formatted['Order'].append(i)

		return formatted


	formatted = DataFrame(format_results(results,state))
	print ggplot(aes(x='Order', y='Value'), data=formatted) + \
    	geom_line(color='green') + \
    	geom_point(color='black') + \
    	ggtitle("Unemployment Data") + \
    	xlab("Month, Year") + \
    	ylab("Value")