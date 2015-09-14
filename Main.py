import json
from AmazonReviewCrawler import AmazonReviewCrawler
from DataSanitizer import DataSanitizer

# Step 1 - Download File into raw_data folder
# AmazonReviewCrawler.downloadReviewsInJsonByProductNameAndPageRange("Certified-Refurbished-Fire-TV-Stick", "B00LO29KXQ", 1, 6181)
# AmazonReviewCrawler.downloadReviewsInJsonByProductNameAndPageRange("Google-Chromecast-Streaming-Media-Player", "B00DR0PDNE", 1, 3664)
# AmazonReviewCrawler.downloadReviewsInJsonByProductNameAndPageRange("Roku-3500R-Streaming-Stick-HDMI", "B00INNP5VU", 1, 709)
# AmazonReviewCrawler.downloadReviewsInJsonByProductNameAndPageRange("Amazon-W87CUN-Fire-TV-Stick", "B00GDQ0RMG", 1, 6189)
# AmazonReviewCrawler.downloadReviewsInJsonByProductNameAndPageRange("Apple-TV-MD199LL-Current-Version", "B007I5JT4S", 1, 701)
# AmazonReviewCrawler.downloadReviewsInJsonByProductNameAndPageRange("Certified-Refurbished-Amazon-Fire-TV", "B00DU15MU4", 1, 3202)

# Step 2 - Clean the data using nltk and combine all the data into single file
DataSanitizer.sanitize()

# Step 3 - Check for duplicates review
no_of_duplicates = 0
reviews_count = {}
reviews = json.load(open("data.json"))
for review in reviews:
	count = reviews_count.get(review["review"], 0)
	count += 1
	reviews_count[review["review"]] = count

# Remove duplicate entry as it was assumed that duplicates are most likely spam
duplicate_reviews = []
for key in reviews_count:
	if(reviews_count[key] > 1):
		no_of_duplicates += 1
		duplicate_reviews.append(key)

unique_reviews = []
for review in reviews:
	if review["review"] not in duplicate_reviews:
		unique_reviews.append(review)

print("No of unique_reviews : ", len(unique_reviews))

f = open('reviews_data.json', 'w')
f.write(json.dumps(unique_reviews))
f.close()