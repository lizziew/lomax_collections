import csv

with open('/Users/elizabethwei/code/exhibit_lomax/public/javascripts/input.csv','r') as csvinput:
    with open('/Users/elizabethwei/code/exhibit_lomax/public/javascripts/output.csv', 'w') as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')
        reader = csv.reader(csvinput)

        all = []
        row = next(reader)
        row.append('latlng')
        all.append(row)

        for row in reader:
            if row[4]=="New Orleans": 
                row.append("29.9511, -90.0715")
            elif row[4]=="Arkabutla":
                row.append("34.7354, -90.0992") 
            elif row[4]=="Bentonia":
                row.append("32.6410, -90.3648")
            elif row[4]=="Canton":
                row.append("40.7989, -81.3784")
            elif row[4]=="Como":
                row.append("34.5107, -89.9398")
            elif row[4]=="Gravel Springs":
                row.append("39.0768, -78.4307")
            elif row[4]=="Greenville":
                row.append("34.8526, -82.3940")
            elif row[4]=="Hollandale":
                row.append("33.1690, -90.8540")
            elif row[4]=="Sardis":
                row.append("34.4371, -89.9159"); 
            all.append(row)

        writer.writerows(all)