import json

txtFile = open('theReviews.txt')

json_string = txtFile.read()

try:
	print(json.loads(json_string))
except ValueError, e:
	print("There is an error in JSON format.")