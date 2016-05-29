import csv
import dateutil.parser as parser

with open('./final.csv','r') as csvinput:
    with open('./output.csv', 'w') as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')
        reader = csv.reader(csvinput)

        all = []
        row = next(reader)
        row.append('timelinedate')
        all.append(row)
        # for row in reader:
        #     if row[4]=="New Orleans": 
        #         row.append("29.9511, -90.0715")
        #     elif row[4]=="Arkabutla":
        #         row.append("34.7354, -90.0992") 
        #     elif row[4]=="Bentonia":
        #         row.append("32.6410, -90.3648")
        #     elif row[4]=="Canton":
        #         row.append("40.7989, -81.3784")
        #     elif row[4]=="Como":
        #         row.append("34.5107, -89.9398")
        #     elif row[4]=="Gravel Springs":
        #         row.append("39.0768, -78.4307")
        #     elif row[4]=="Greenville":
        #         row.append("34.8526, -82.3940")
        #     elif row[4]=="Hollandale":
        #         row.append("33.1690, -90.8540")
        #     elif row[4]=="Sardis":
        #         row.append("34.4371, -89.9159"); 
        #     all.append(row)

        for row in reader:
        	if len(row) <= 5:
        		continue 
        	text = row[5]
        	if text[0:2]=="00":
        		text = "01-01-" + text[6:10]
    		date = (parser.parse(text))
    		row.append(date.isoformat()); 
        	all.append(row)

        writer.writerows(all)



# text = 'Thu, 16 Dec 2010 12:14:05 +0000'
# date = (parser.parse(text))
# print(date.isoformat())
# 2010-12-16T12:14:05+00:00
