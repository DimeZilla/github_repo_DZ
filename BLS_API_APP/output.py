#This script estabilishes different ways to output the data once retrieved

def data_output(data, chart_title):
		print "Good News! You're data has been returned. I'm happy to show it to you."
		print "Just tell me how you want it - Table or Line Graph?"

		data_output = raw_input("Choose table or line > ")

		if data_output[0].lower() == "t":
			print "Ok, here's your data."
			print data
		elif data_output[0] == "l" or data_output[0].lower() =="g":
			import ggplot as gg 

			plot = gg.ggplot(gg.aes(x='Month, Year', y='Value'), data=data) + \
    			gg.geom_point(color='black') + \
    			gg.geom_line(color='green') + \
    			gg.ggtitle(chart_title) + \
    			gg.xlab("Month, Year") + \
    			gg.ylab("Value") 
    			gg.scale_x_date(breaks = gg.date_breaks('1 month'), labels= gg.date_format("%B"))

			print (plot + gg.theme_xkcd())
			