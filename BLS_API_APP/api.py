#	Connect to BLS API
#	Retrieve monthly unemployment rates and raw numbers going back 10 years by
		# A. State
		# B. county
	#	Return results 
	
def get_data(series_id, start_year, end_year):
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
	return results
