#This is a dictionary for BLS Series IDs
# LASST010000000000003, LASST010000000000004, LASST010000000000005, LASST010000000000006
# "LAU{0}{1}0000000003", "LAU{0}{1}0000000000004", "LAU{0}{1}0000000000005", "LAU{0}{1}0000000000006"

#BLS API EXAMPLES

## SINGLE SERIES ##
# HTTP Type:	GET
# URL:	http://api.bls.gov/publicAPI/v1/timeseries/data/<series_id>
# Payload:	series_id
# Example Payload:	
# LAUCN21219003

## MULTIPLE SERIES ##
# HTTP Type:	POST
# URL:	http://api.bls.gov/publicAPI/v1/timeseries/data/
# Payload:	JSON Payload:
# {"seriesid":["Series1",  ...,  "SeriesN"]}
# Example Payload:	
# {"seriesid":["LAUCN21219003",  "LAUCN21219004"]}

## SPECIFYING YEARS ##
# HTTP Type:	POST
# URL:	http://api.bls.gov/publicAPI/v1/timeseries/data/
# Payload:	JSON Payload:
# {"seriesid":["Series1", ...,  "SeriesN"], 
# "startyear":"yearX",  
# "endyear":"yearY"
# }
# Example Payload:	
# {"seriesid":["LAUCN21219003",  "LAUCN21219004"], 
# "startyear":"2010", 
# "endyear":"2012"
# }

state_fips = {
'Alabama': '01','Alaska': '02','Arizona': '04','Arkansas': '05','California': '06','Colorado': '08','Connecticut': '09','Delaware': '10',
'Florida': '12','Georgia': '13','Hawaii': '15','Idaho': '16','Illinois': '17','Indiana': '18','Iowa': '19','Kansas': '20','Kentucky': '21',
'Louisiana': '22','Maine': '23','Maryland': '24','Massachusetts': '25','Michigan': '26','Minnesota': '27','Mississippi': '28','Missouri': '29',
'Montana': '30','Nebraska': '31','Nevada': '32','New Hampshire': '33','New Jersey': '34','New Mexico': '35','New York': '36','North Carolina': '37',
'North Dakota': '38','Ohio': '39','Oklahoma': '40','Oregon': '41','Pennsylvania': '42','Rhode Island': '44','South Carolina': '45','South Dakota': '46',
'Tennessee': '47','Texas': '48','Utah': '49','Vermont': '50','Virginia': '51','Washington': '53','West Virginia': '54','Wisconsin': '55','Wyoming': '56',
 }

county_fips = {}

time_series = ('2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011',
		'2012','2013','2014')