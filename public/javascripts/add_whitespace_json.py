import json

with open("/Users/elizabethwei/code/exhibit_lomax/public/javascripts/clean.json", "r") as jsoninput:
    data = json.load(jsoninput)

for d in data:
	if d=="items":
		for o in data[d]:
			for key in o:
				if key=="showtitle" or key=="topic":
					o[key] = o[key] + " "

with open("/Users/elizabethwei/code/exhibit_lomax/public/javascripts/clean.json", "w") as jsonoutput:
    jsonoutput.write(json.dumps(data))