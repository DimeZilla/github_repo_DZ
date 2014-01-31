#	Connect to BLS API
#	Retrieve monthly unemployment rates and raw numbers going back 10 years by
		# A. State
		# B. county
	#	Return results 

from pandas import DataFrame
from series_id_dict import month_series
from datetime import date

# GET_DATA INPUT EXAMPLE: 
# series_id = 'LASST010000000000003'
# start_year = '2010'
# end_year = '2013'
# state = 'Florida'
	
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
		for i in range(len(dump)-1,-1,-1):			
			if dump[i]["periodName"] == 'Annual':
				dump.pop(i)
			else:
				pass
		
		#format returned data into a dictionary
		formatted = {'State': list(), 'Value': list(), 'Month, Year': list(), 'Preliminary?': list()}
		for i in range(len(dump)-1,-1,-1):
			formatted['State'].append(state)
			formatted['Value'].append(dump[i]["value"])
			formatted['Month, Year'].append(date(year=int(dump[i]["year"]), month = int(month_series[dump[i]["periodName"]]), day=01))
			if "code" in dump[i]["footnotes"][0]:
				if dump[i]["footnotes"][0]["code"] == "P":
					formatted['Preliminary?'].append("Y")
			else:
				formatted['Preliminary?'].append("N")
		return formatted


	formatted = DataFrame(format_results(results,state))	

	return formatted
    	