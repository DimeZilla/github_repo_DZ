#	Connect to BLS API
#	Retrieve monthly unemployment rates and raw numbers going back 10 years by
		# A. State
		# B. county
	#	Return results 
	
def get_data(series_id, start_year, end_year, state):
	from urllib2 import Request, urlopen
	from urllib import urlencode
	import json
	#this requires the python tabulate package
	# simply run on your command line terminal 'pip install tabulate'
	from tabulate import tabulate 


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
		ptest = dump[0]["footnotes"][0]["code"] ## Will equal "P"
		
		formatted = list()
		formatted.append(["State","Month","Year","Value"])	
		for i in range(len(dump)-1,-1,-1):
			formatted.append([state,str(dump[i]["periodName"]), str(dump[i]["year"]), str(dump[i]["value"])])

		return formatted


	formatted = format_results(results, state)
	print tabulate(formatted)
	
