import glob
import json
import nltk

from nltk import word_tokenize

class DataSanitizer:

	@staticmethod
	def sanitize():
		reviews = []
		total_reviews = 0

		raw_files_urls = glob.glob("raw_data/*.json")
		
		for raw_files_url in raw_files_urls:
			raw_reviews = json.load(open(raw_files_url))

			total_reviews += len(raw_reviews)

			# Clean the review data and author name using NLTK 
			for review in raw_reviews:
				tokens = word_tokenize(review["review"])

				if(len(tokens) > 130):
					reviews.append(review)

		print("Filtered Reviews : ", len(reviews))
		print("Total Reviews : ", total_reviews)

		f = open('data.json', 'w')
		f.write(json.dumps(reviews))
		f.close()